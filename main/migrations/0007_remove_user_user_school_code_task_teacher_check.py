# Generated by Django 4.2.5 on 2023-11-12 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_user_user_school_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_school_code',
        ),
        migrations.AddField(
            model_name='task',
            name='teacher_check',
            field=models.BooleanField(default=False, verbose_name='Нужна проверка?'),
        ),
    ]
