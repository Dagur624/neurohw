from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("lk", views.lk, name="lk"),  # type: ignore
    path("accounts/signup", views.signup, name = "signup"),
    path("lk/teacher_classes", views.teacher_class, name="teacher_classes"),
    path("lk/teacher_classes/<int:id>", views.class1, name="teacher_class"),
    path("lk/create_task", views.create_task, name= "create_task"),
    path("lk/give_task", views.give_task, name= "give_task"),
    path("lk/teacher_classes/student_task_list/<int:student_id>", views.student_task_list_teacher, name = "student_task_list_teacher"),
    path("lk/teacher_classes/student_task/<int:task_id>", views.student_task_teacher, name="student_task_teacher"),
    path("lk/student_task_list/<int:status>", views.student_task_list, name="student_task_list"),
    path("lk/student_task/<int:student_task_id>", views.student_task_do, name="student_task_do"),
    path("lk/student_teacher_list", views.student_teacher_list, name="student_teacher_list")
]
