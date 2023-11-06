from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _


class Info(models.Model):
    class Sex(models.TextChoices):
        FEMALE = "F", _("Female")
        MALE = "M", _("Male")

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sex = models.CharField(max_length=1, choices=Sex.choices, default=Sex.FEMALE)
    birthday = models.DateField(null=True)

    def __str__(self):
        return self.user.first_name

    class Meta:
        verbose_name = 'Информация'
        verbose_name_plural = 'Информация'


class Record(models.Model):
    date = models.DateField(null=False)
    name = models.CharField(null=False, max_length=255)
    description = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    planned_time = models.TimeField(null=False)
    actual_time = models.TimeField(null=True, default="00:00")
    reason = models.TextField(null=True, default="Задача не завершена")
    progress = models.DecimalField(max_digits=3, decimal_places=2, default=0,
                                   validators=[MinValueValidator(0), MaxValueValidator(1)])
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Log(models.Model):
    record = models.ForeignKey("Record", on_delete=models.RESTRICT)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    old_data = models.JSONField()
    new_data = models.JSONField()

    def __str__(self):
        return self.record.name

    class Meta:
        verbose_name = 'История'
        verbose_name_plural = 'История'
