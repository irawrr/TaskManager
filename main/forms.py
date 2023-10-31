from .models import Task
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task", "time"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
            "time": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите плановое время выполнения'
            }),
        }

