# Generated by Django 4.2.6 on 2023-11-03 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_task_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='time',
            field=models.TimeField(verbose_name='Время на выполнение'),
        ),
    ]
