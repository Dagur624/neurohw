# Generated by Django 4.2.7 on 2023-12-03 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_studenttask_done_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studenttask',
            name='limite_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Лимит выполнения'),
        ),
    ]
