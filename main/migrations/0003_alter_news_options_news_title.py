# Generated by Django 4.2.5 on 2023-10-08 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_grade_student_subject_usertype_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AddField(
            model_name='news',
            name='title',
            field=models.CharField(default='', max_length=255, verbose_name='Заголовок'),
        ),
    ]
