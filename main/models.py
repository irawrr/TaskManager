from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')
    time = models.TimeField('Время на выполнение')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sex = models.BooleanField(default=False)  # male = False, female = True
    birthday = models.DateField(null=True)


class Record(models.Model):
    date = models.DateField(null=False)
    name = models.CharField(null=False, max_length=255)
    description = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    planned_time = models.TimeField(null=False)
    actual_time = models.TimeField(null=True)
    reason = models.TextField(null=True)
    progress = models.DecimalField(max_digits=3, decimal_places=2, default=0,
                                   validators=[MinValueValidator(0), MaxValueValidator(1)])
    created_at = models.DateTimeField(auto_now_add=True)


class Log(models.Model):
    record = models.ForeignKey("Record", on_delete=models.RESTRICT)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    old_data = models.JSONField()
    new_data = models.JSONField()
