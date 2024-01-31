from django.shortcuts import render
from . import models
from django.shortcuts import redirect
from django.urls import reverse
from . import forms
from datetime import date, datetime, timedelta
from . import utils


def index(request):
    news = models.News.objects.all()
    return render(request, "index.html", {
        "news": news
    })


def lk(request):
    if not request.user.is_authenticated:
        return redirect(reverse("index"))
    if request.user.user_type.code == 'student':
        return render(request, "lk_student.html")
    elif request.user.user_type.code == 'teacher':

        return render(request, "lk_teacher.html")


def teacher_class_list(request):
    grades = models.Grade.objects.all()
    return render(request, "teacher_class_list.html", {
        "grades": grades
    })


def teacher_class(request, id):
    grade = models.Grade.objects.get(id=id)
    students = models.Student.objects.filter(grade__id=id)
    students_dict = []
    start_date = datetime.today() - timedelta(days=60)
    for student in students:
        students_dict.append({"student": student, **utils.student_result_base(student.user, start_date)})
    return render(request, "teacher_class.html", {
        "class": grade,
        "students": students_dict,

    })


def create_task(request):
    if request.method == "POST":
        print("POST")
        form = forms.CreateTaskForm(request.POST)
        if form.is_valid():
            print("valid")
            form.save()
            return redirect(reverse("lk"))
    else:
        form = forms.CreateTaskForm()
    return render(request, "create_task.html", {
        "form": form
    })


def give_task(request):
    if request.method == "POST":
        form = forms.GiveTaskForm(request.POST)
        if form.is_valid():
            for student_id in form.cleaned_data["students"]:
                student_task_primer = form.save(commit=False)
                student = models.Student.objects.get(id=student_id)
                student_task = models.StudentTask(limite_date=student_task_primer.limite_date, student=student,
                                                  teacher=models.Teacher.objects.get(id=request.user.id),
                                                  task_id=student_task_primer.task_id)
                student_task.save()
            return redirect(reverse("lk"))
    form = forms.GiveTaskForm()
    return render(request, "create_task.html", {
        "form": form
    })


def student_task_list_teacher(request, student_id):
    student = models.Student.objects.get(id=student_id)
    tasks = models.StudentTask.objects.filter(student__id=student_id)
    return render(request, "student_task_list_teacher.html", {
        "tasks": tasks,
        "student": student
    })


def student_task_teacher(request, task_id):
    task = models.StudentTask.objects.get(id=task_id)
    if request.method == "POST":
        form = forms.CheckTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
    form = forms.CheckTaskForm(instance=task)
    return render(request, "student_task_teacher.html", {
        "task": task,
        "form": form
    })


def student_task_list(request, status):
    subject_checked = request.GET.get("subject")
    student = models.Student.objects.get(user=request.user)
    tasks = models.StudentTask.objects.filter(student=student)
    if subject_checked:
        tasks = tasks.filter(task__subject__code=subject_checked)
    if status == 0:  # Не сделано
        tasks = tasks.filter(student_answer="")
    elif status == 1:  # Сделано, но не проверено
        tasks = tasks.exclude(student_answer="").filter(is_right=None)
    elif status == 2:  # Сделано и проверено
        tasks = tasks.exclude(is_right=None)
    subjects = models.Subject.objects.all()
    return render(request, "student_task_list.html", {
        "student": student,
        "tasks": tasks,
        "status": status,
        "subjects": subjects
    })


def student_task_do(request, student_task_id=0):
    if student_task_id != 0:
        student_task = models.StudentTask.objects.get(id=student_task_id)
    else:
        student_task = models.StudentTask.objects.filter(student__user__id=request.user.id, student_answer="").first()
        if not student_task:
            return redirect(reverse('student_task_list', args=[0]))
    if request.method == "POST":
        form = forms.DoTaskForm(request.POST, instance=student_task)
        if form.is_valid():
            save_task = form.save(commit=False)
            if not save_task.teacher_check:

                if save_task.student_answer == save_task.task.answer:
                    save_task.is_right = True
                else:
                    save_task.is_right = False
            save_task.save()
    form = forms.DoTaskForm(instance=student_task)
    return render(request, "student_task_do.html", {
        "student_task": student_task,
        "form": form
    })


def student_teacher_list(request):
    teachers = models.Teacher.objects.all()
    print(teachers)
    return render(request, "student_teacher_list.html", {
        "teachers": teachers
    })


def signup(request):
    if request.method == "POST":
        form = forms.CustomSignupForm(request.POST)
        if form.is_valid():
            grade_id = form['grade'].value()
            print(grade_id)
            account = form.save(request)
            if account.user_type.code == "teacher":
                models.Teacher(user=account).save()
            if account.user_type.code == "student":
                grade = models.Grade.objects.get(id=grade_id)
                models.Student(user=account, grade=grade).save()
            return redirect(reverse("account_login"))
    form = forms.CustomSignupForm()
    return render(request, "account/signup.html", {
        'form': form
    })


def student_result(request):
    student_tasks = {}
    date_format = '%d.%m.%Y'
    if request.method == "POST":
        form = forms.ResultDateForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data["start_date"]
            end_date = form.cleaned_data["end_date"]
            student_tasks = utils.student_result_base(request.user, start_date, end_date)
    else:
        form = forms.ResultDateForm()
    return render(request, "student_result.html", {
        'form': form,
        **student_tasks
    })

# Create your views here.
