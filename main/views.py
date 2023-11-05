from django.shortcuts import render
from . import models
from django.shortcuts import redirect
from django.urls import reverse
from . import forms
def index(request):
    news = models.News.objects.all()
    return render(request, "index.html", {
        "news":news
    })
def lk(request):
    if not request.user.is_authenticated:
        return redirect(reverse("index"))
    if request.user.user_type.code == 'student':
        return render(request, "lk_student.html")
    elif request.user.user_type.code == 'teacher':

        return render(request, "lk_teacher.html")
def teacher_class(request):
    grades = models.Grade.objects.all()
    return render(request, "teacher_class.html", {
        "grades": grades
    })
def class1(request, id):
    class1 = models.Grade.objects.get(id = id)
    students = models.Student.objects.filter(grade__id = id)
    return render(request, "class1.html", {
        "class":class1,
        "students":students
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
        "form":form
    })
    
def give_task(request):
    if request.method == "POST":
        print("POST")
        form = forms.GiveTaskForm(request.POST)
        if form.is_valid():
            print("valid")
            for student_id in form.cleaned_data["students"]:
                student_task_primer = form.save(commit = False)
                student = models.Student.objects.get(id = student_id)
                student_task = models.StudentTask(limite_date = student_task_primer.limite_date, student = student, 
                                                  teacher = models.Teacher.objects.get(id = request.user.id), 
                                                  task_id = student_task_primer.task_id)
                student_task.save()
            return redirect(reverse("lk"))
    else:
        form = forms.GiveTaskForm()
    return render(request, "create_task.html", {
        "form":form
    })
        
# Create your views here.
