# Generated by Django 4.2.5 on 2023-11-12 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_task_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='studenttask',
            name='done_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата выполнения'),
        ),
    ]
