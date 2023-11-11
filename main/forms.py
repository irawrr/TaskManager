from django import forms
from .models import Record, User
from django.forms import ModelForm, TextInput, Textarea, PasswordInput


class DateInput(forms.DateInput):
    input_type = "date"


class TimeInput(forms.DateInput):
    input_type = "time"


class CheckBox(forms.CheckboxInput):
    input_type = "checkbox"


class RecordForm(ModelForm):
    class Meta:
        model = Record
        fields = ["date", "name", "description", "planned_time"]
        widgets = {
            "date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите дату'
            }),
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
            "planned_time": TimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите плановое время выполнения'
            }),
        }


class ResultForm(ModelForm):
    class Meta:
        model = Record
        fields = ["actual_time", "reason", "progress"]
        widgets = {
            "actual_time": TimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите фактическое время выполнения'
            }),
            "reason": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите причины расхождений'
            }),
            "progress": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите прогресс'
            }),
        }


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username", "password", "is_superuser"]
        widgets = {
            "first_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }),
            "last_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите фамилию'
            }),
            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите почту'
            }),
            "username": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите логин'
            }),
            "password": PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите пароль'
            }),
            "is_superuser": CheckBox(attrs={
                'class': 'required checkbox form-control',
            }),
        }