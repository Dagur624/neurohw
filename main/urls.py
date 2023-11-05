from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("lk", views.lk, name="lk"),
    path("lk/teacher_classes", views.teacher_class, name="teacher_classes"),
    path("lk/teacher_classes/<int:id>", views.class1, name="teacher_class"),
    path("lk/create_task", views.create_task, name= "create_task"),
    path("lk/give_task", views.give_task, name= "give_task")
]
