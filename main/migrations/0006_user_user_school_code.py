# Generated by Django 4.2.5 on 2023-10-21 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_theme_task_theme'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_school_code',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='Код, выдаваемый школой'),
        ),
    ]
