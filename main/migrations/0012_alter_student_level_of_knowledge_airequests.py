# Generated by Django 4.2.7 on 2024-03-20 08:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_studenttask_teaher_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='level_of_knowledge',
            field=models.IntegerField(default=0, verbose_name='Уровень знаний'),
        ),
        migrations.CreateModel(
            name='AIRequests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request', models.TextField(verbose_name='Запрос')),
                ('human_answer', models.TextField(blank=True, default='', verbose_name='Ответ человека')),
                ('ai_answer', models.TextField(blank=True, default='', verbose_name='Ответ нейросети')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('request_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Сгенерированное задание',
                'verbose_name_plural': 'Сгенерированные задания',
            },
        ),
    ]
