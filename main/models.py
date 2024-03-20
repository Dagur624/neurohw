from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserType(models.Model):
    name = models.CharField("Имя", max_length=15)
    code = models.CharField("Код", max_length=15)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Тип пользователя'
        verbose_name_plural = "Типы пользователей"


class User(AbstractUser):
    user_type = models.ForeignKey(UserType, verbose_name="Тип пользователя", on_delete=models.SET_NULL, blank=True,
                                  null=True)
    phone_number = models.CharField("Телефон", max_length=15, blank=True, null=True)

    def __str__(self) -> str:
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = "Пользователи"


class Grade(models.Model):
    number = models.IntegerField("Класс")
    letter = models.CharField("Буква класса", max_length=1)

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = "Классы"

    def __str__(self) -> str:
        return str(self.number) + " " + self.letter


class Student(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE, unique=True)
    grade = models.ForeignKey(Grade, verbose_name="Класс", on_delete=models.CASCADE)
    level_of_knowledge = models.IntegerField("Уровень знаний", default=0)

    def __str__(self) -> str:
        return str(self.user)

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = "Ученики"


class News(models.Model):
    title = models.CharField("Заголовок", max_length=255, default="")
    text = models.TextField("Текст")
    date = models.DateTimeField("Дата", auto_now=True)
    create_user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = "Новости"


class Subject(models.Model):
    name = models.CharField("Предмет", max_length=255)
    code = models.CharField("Код", max_length=255)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = "Предметы"


class Teacher(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE, unique=True)

    def __str__(self) -> str:
        return str(self.user)

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = "Учителя"


class TeacherSubject(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, verbose_name="Предмет", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.user) + "<->" + str(self.subject)

    class Meta:
        verbose_name = 'Предмет учителя'
        verbose_name_plural = "Предметы учителей"


class StudentParent(models.Model):
    student = models.ForeignKey(Student, verbose_name="Ученик", on_delete=models.CASCADE)
    parent = models.ForeignKey(User, verbose_name="Родитель", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.student) + "<->" + str(self.parent)

    class Meta:
        verbose_name = 'Родитель ученика'
        verbose_name_plural = "Родители учеников"


class Theme(models.Model):
    name = models.CharField("Название темы", max_length=255, default="")
    code = models.CharField("Код темы", max_length=255, default="")
    subject = models.ForeignKey(Subject, verbose_name="Предмет темы", on_delete=models.CASCADE)
    parent = models.ForeignKey("Theme", verbose_name="Родительский объект", null=True, blank=True,
                               on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = "Темы"


class Task(models.Model):
    name = models.CharField("Название", max_length=255, default="")
    grade = models.IntegerField("Класс")
    level_of_knowledge = models.IntegerField("Уровень знаний")
    task_text = models.TextField("Текст задания")
    answer = models.CharField("Ответ", max_length=255, null=True, blank=True)
    subject = models.ForeignKey(Subject, verbose_name="Предмет", on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, verbose_name="Тема", on_delete=models.CASCADE, null=True, blank=True)
    is_neural = models.BooleanField("Написано нейросетью?", default=False)
    teacher_check = models.BooleanField("Нужна проверка?", default=False)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = "Задания"


class StudentTask(models.Model):
    task = models.ForeignKey(Task, verbose_name='Задание', on_delete=models.CASCADE)
    student = models.ForeignKey(Student, verbose_name="Ученик", on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, verbose_name="Учитель", on_delete=models.CASCADE)
    student_answer = models.TextField("Ответ ученика")
    is_right = models.BooleanField("Правильно?", blank=True, null=True)
    teacher_check = models.BooleanField("Нужна проверка?", default=False)
    teaher_comment = models.TextField("Комментарий учителя", blank=True, null=True)
    get_date = models.DateTimeField("Дата выдачи", auto_now_add=True)
    done_date = models.DateTimeField("Дата выполнения", null=True, blank=True)
    limite_date = models.DateTimeField("Лимит выполнения", null=True, blank=True)

    def __str__(self) -> str:
        return str(self.task) + "<->" + str(self.student)

    class Meta:
        verbose_name = 'Задание ученика'
        verbose_name_plural = "Задания учеников"


class AIRequests(models.Model):
    request_user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    request = models.TextField("Запрос")
    human_answer = models.TextField("Ответ человека", default="", blank=True)
    ai_answer = models.TextField("Ответ нейросети", default="", blank=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.request_user.username} - {self.request}"

    class Meta:
        verbose_name = 'Сгенерированное задание'
        verbose_name_plural = "Сгенерированные задания"
