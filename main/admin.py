from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
admin.site.register(models.User, UserAdmin)
admin.site.register(models.UserType)
admin.site.register(models.Student)
admin.site.register(models.StudentParent)
admin.site.register(models.Grade)
admin.site.register(models.News)
admin.site.register(models.Teacher)
admin.site.register(models.TeacherSubject)
admin.site.register(models.Subject)
admin.site.register(models.Task)
admin.site.register(models.StudentTask)


# Register your models here.
