from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


@login_required
def change(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/change.html', {'title': 'Текущие задачи', 'tasks': tasks})

@login_required
def report(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/report.html', {'title': 'Текущие задачи', 'tasks': tasks})

@login_required
def users(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/users.html', {'title': 'Пользователи', 'tasks': tasks})

@login_required
def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Текущие задачи', 'tasks': tasks})

@login_required
def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'
    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)

@login_required
def delete(request, pk):
    try:
        obj = Task.objects.get(pk=pk)
        obj.delete()
        return redirect('home')
    except Task.DoesNotExist:
        return redirect('home')
