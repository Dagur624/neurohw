# Generated by Django 4.2.7 on 2023-12-03 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_studenttask_limite_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studenttask',
            name='teaher_comment',
            field=models.TextField(blank=True, null=True, verbose_name='Комментарий учителя'),
        ),
    ]