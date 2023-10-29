from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
class PersonAdmin(UserAdmin):
    fieldsets = [(None, {'fields': ('username', 'password')}), 
                 ('Персональная информация', {'fields': ('first_name', 'last_name', 'email')}), 
                 ('Права доступа', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}), 
                 ('Важные даты', {'fields': ('last_login', 'date_joined')}),
                 ('Дополнительные данные', {'fields': ('phone_number', "user_type")})]
admin.site.register(models.User, PersonAdmin)
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
admin.site.register(models.Theme)


# Register your models here.
