# Generated by Django 4.2.6 on 2023-11-12 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_delete_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='on_delete',
            field=models.BooleanField(default=False),
        ),
    ]
