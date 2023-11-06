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

