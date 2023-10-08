from django.db import models
from django.contrib.auth.models import AbstractUser

class UserType(models.Model):
    name = models.CharField("Имя", max_length=15)
    code = models.CharField("Код", max_length=15)

class User(AbstractUser):
    user_type = models.ForeignKey(UserType, verbose_name="Тип пользователя", on_delete=models.SET_NULL, blank=True, null=True)
    phone_number = models.CharField("Телефон", max_length=15, blank=True, null=True)

class Grade(models.Model):
    number = models.IntegerField("Класс")
    letter = models.CharField("Буква класса", max_length=1)

class Student(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE, unique=True)
    grade = models.ForeignKey(Grade, verbose_name="Класс", on_delete=models.CASCADE)
    level_of_knowledge = models.IntegerField("Уровень знаний")

class News(models.Model):
    title = models.CharField("Заголовок", max_length=255, default="")
    text = models.TextField("Текст")
    date = models.DateTimeField("Дата", auto_now=True)
    create_user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.SET_NULL, blank=True, null=True)
    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name= 'Новость'
        verbose_name_plural = "Новости"

class Subject(models.Model):
    name = models.CharField("Предмет", max_length=255)
    code = models.CharField("Код", max_length=255)

class Teacher(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE, unique=True)
    
class TeacherSubject(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, verbose_name="Предмет", on_delete=models.CASCADE)

class StudentParent(models.Model):
    student = models.ForeignKey(Student, verbose_name="Ученик", on_delete=models.CASCADE)
    parent = models.ForeignKey(User, verbose_name="Родитель", on_delete=models.CASCADE)

class Task(models.Model):
    grade = models.IntegerField("Класс")
    level_of_knowledge = models.IntegerField("Уровень знаний")
    task_text = models.TextField("Текст задания")
    answer = models.CharField("Ответ", max_length=255)
    subject = models.ForeignKey(Subject, verbose_name="Предмет", on_delete=models.CASCADE)
    is_neural = models.BooleanField("Написано нейросетью?", default=False)

class StudentTask(models.Model):
    task = models.ForeignKey(Task, verbose_name='Задание', on_delete=models.CASCADE)
    student = models.ForeignKey(Student, verbose_name="Ученик", on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, verbose_name="Учитель", on_delete=models.CASCADE)
    student_answer = models.TextField("Ответ ученика")
    is_right = models.BooleanField("Правильно?", blank=True, null=True)
    teacher_check = models.BooleanField("Нужна проверка?", default=False)
    teaher_comment = models.TextField("Комментарий учителя")
    get_date = models.DateTimeField("Дата выдачи", auto_now_add=True)
    limite_date = models.DateTimeField("Лимит выполнения") 