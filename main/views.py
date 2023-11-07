from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Record
from .forms import RecordForm, ResultForm


@login_required
def change(request):
    if request.method == "POST":
        data = request.POST
        password = data.get("password")
        password2 = data.get("password2")
        if password == password2:
            user = request.user
            user.set_password(password)
            user.save()
    tasks = Record.objects.order_by('-id')
    return render(request, 'main/change.html', {'title': 'Сменить пароль', 'tasks': tasks})


@login_required
def report(request):
    tasks = Record.objects.order_by('-id')
    return render(request, 'main/report.html', {'title': 'Отчёт', 'tasks': tasks})


@login_required
def users(request):
    tasks = Record.objects.order_by('-id')
    return render(request, 'main/users.html', {'title': 'Пользователи', 'tasks': tasks})


@login_required
def index(request):
    tasks = Record.objects.order_by('-id').filter(user=request.user)
    return render(request, 'main/index.html', {'title': 'Текущие задачи', 'tasks': tasks})


@login_required
def create(request):
    error = ''
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.user = request.user
            record.save()
            form.save()
            return redirect('home')
        else:
            error = 'Введите корректные данные!'
    form = RecordForm()
    context = {
        'form': form,
        'error': error,
        'title': "Создание задачи",
        'button_name': "Создать"
    }
    return render(request, 'main/create.html', context)


@login_required
def delete(request, pk):
    try:
        obj = Record.objects.get(pk=pk)
        obj.delete()
        return redirect('home')
    except Record.DoesNotExist:
        return redirect('home')


@login_required
def edit(request, pk):
    error = ''
    task = Record.objects.get(pk=pk)
    if request.method == "POST":
        form = RecordForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return redirect('home')
        else:
            error = 'Введите корректные данные!'
    else:
        form = RecordForm(instance=task)
    context = {
        'form': form,
        'error': error,
        'title': "Редактирование задачи",
        'button_name': "Редактировать"
    }
    return render(request, 'main/create.html', context)

@login_required
def complete(request, pk):
    error = ''
    task = Record.objects.get(pk=pk)
    if request.method == "POST":
        form = ResultForm(request.POST, instance=task)
        if form.is_valid():
            task.is_completed = True
            task = form.save(commit=False)
            task.save()
            return redirect('home')
        else:
            error = 'Введите корректные данные!'
    else:
        form = ResultForm(instance=task)
    context = {
        'form': form,
        'error': error,
        'title': "Завершение задачи",
        'button_name': "Завершить"
    }
    return render(request, 'main/complete.html', context)