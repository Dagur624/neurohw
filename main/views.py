from django.shortcuts import render
from . import models
from django.shortcuts import redirect
from django.urls import reverse
from .forms import CreateTaskForm
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
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            print("valid")
            form.save()
            return redirect(reverse("lk"))
    else:
        form = CreateTaskForm()
    return render(request, "create_task.html", {
        "form":form
    })
        
# Create your views here.
