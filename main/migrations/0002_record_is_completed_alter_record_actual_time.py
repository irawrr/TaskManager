# Generated by Django 4.2.6 on 2023-11-06 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='record',
            name='actual_time',
            field=models.TimeField(default='00:00', null=True),
        ),
    ]
