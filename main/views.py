from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Record, User
from .forms import RecordForm, ResultForm
from datetime import *


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
    data = request.GET
    today = date.today()
    min_year = 2020
    year = data.get('year', default='')
    year = int(year) if str.isdigit(year) else 0
    week_num = data.get('week', default='')
    week_num = int(week_num) if str.isdigit(week_num) else 0
    if week_num < 1 or week_num > 52:
        week_num = today.isocalendar().week
    if year < min_year:
        year = today.year
    week_start = date.fromisocalendar(year, week_num, 1)
    week_end = week_start + timedelta(days=6)
    tasks = Record.objects.filter(date__gte=week_start).filter(date__lte=week_end).order_by('id')
    users = User.objects.order_by('id')
    return render(request, 'main/report.html', {
        'title': 'Отчёт',
        'days': [
            'monday',
            'tuesday',
            'wednesday',
            'thursday',
            'friday',
            'saturday',
            'sunday',
        ],
        'data': {
            'monday': {
                'date': week_start,
                'tasks': list(tasks.filter(date__iso_week_day=1).all()),
            },
            'tuesday': {
                'date': week_start + timedelta(days=1),
                'tasks': list(tasks.filter(date__iso_week_day=2).all()),
            },
            'wednesday': {
                'date': week_start + timedelta(days=2),
                'tasks': list(tasks.filter(date__iso_week_day=3).all()),
            },
            'thursday': {
                'date': week_start + timedelta(days=3),
                'tasks': list(tasks.filter(date__iso_week_day=4).all()),
            },
            'friday': {
                'date': week_start + timedelta(days=4),
                'tasks': list(tasks.filter(date__iso_week_day=5).all()),
            },
            'saturday': {
                'date': week_start + timedelta(days=5),
                'tasks': list(tasks.filter(date__iso_week_day=6).all()),
            },
            'sunday': {
                'date': week_end,
                'tasks': list(tasks.filter(date__iso_week_day=7).all()),
            },
        },
        'week': {
            'number': week_num,
            'start': week_start,
            'end': week_end,
            'urls': {
                'prev': request.path + "?year={year}&week={week}".format(
                    year=year if week_num > 1 or year == min_year else year - 1,
                    week=week_num - 1 if week_num > 1 else 52 if year > min_year else 1,
                ),
                'next': request.path + "?year={year}&week={week}".format(
                    year=year if week_num < 52 else year + 1,
                    week=week_num + 1 if week_num < 52 else 1,
                ),
            },
        },
        'users': list(users.all()),
    })


@login_required
def users(request):
    tasks = Record.objects.order_by('-id')
    return render(request, 'main/users.html', {'title': 'Пользователи', 'tasks': tasks})


@login_required
def index(request):
    tasks = Record.objects.order_by('date').filter(user=request.user, date__gte=date.today())
    dates = Record.objects.values_list('date', flat=True).distinct().order_by('date').filter(date__gte=date.today())
    try:
        date_string = request.GET.get('date')
        selected_date = datetime.strptime(date_string, '%Y-%m-%d').date()
        tasks = tasks.filter(date=selected_date)
    except:
        selected_date = None
    return render(request, 'main/index.html', {
        'title': 'Текущие задачи',
        'tasks': tasks,
        'dates': dates,
        'selected_date': selected_date,
    })

@login_required
def create(request):
    error = ''
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid() and form.cleaned_data['date'] >= datetime.now().date():
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
        if form.is_valid() and form.cleaned_data['date'] >= datetime.now().date():
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
