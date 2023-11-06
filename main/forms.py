from .models import Record
from django.forms import ModelForm, TextInput, Textarea


class RecordForm(ModelForm):
    class Meta:
        model = Record
        fields = ["date", "name", "description", "planned_time"]
        widgets = {
            "date": TextInput(attrs={
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
            "planned_time": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите плановое время выполнения'
            }),
        }


class ResultForm(ModelForm):
    class Meta:
        model = Record
        fields = ["actual_time", "reason", "progress"]
        widgets = {
            "actual_time": TextInput(attrs={
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
