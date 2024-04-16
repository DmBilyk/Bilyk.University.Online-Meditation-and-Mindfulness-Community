from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import TaskForm, EventForm
from .models import Task, Event
import datetime
from WEB.decorators import custom_login_required
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@custom_login_required
def add_event(request):
    try:
        if request.method == 'POST':
            form = EventForm(request.POST)
            if form.is_valid():
                event = form.save(commit=False)
                event.user = request.user
                event.save()
                return redirect('calendar')
        else:
            form = EventForm()
        return render(request, 'calendar/add_event.html', {'form': form})
    except Exception as e:
        logger.error(e)
        return render(request, 'calendar/add_event.html', {'form': form})


@custom_login_required
def calendar_view(request):
    try:
        today = timezone.now().date()
        tasks = Task.objects.filter(user=request.user).filter(
            Q(time__gte=timezone.now().time()) | Q(time__lt=timezone.now().time())
        )
        completed_tasks_count = Task.objects.filter(user=request.user, completed=True).count()
        overdue_tasks = Task.objects.filter(user=request.user, completed=False, time__lt=timezone.now().time())
        for task in overdue_tasks:
            messages.warning(request, f'Task "{task.description}" is overdue.')
        first_task = request.user.task_set.first()
        if first_task is not None:
            last_reset_time = first_task.last_reset
            if timezone.now() - last_reset_time > timezone.timedelta(hours=24):
                Task.objects.filter(user=request.user).update(completed=False, last_reset=timezone.now())
        selected_date = request.GET.get('date')
        if selected_date:
            selected_date = datetime.strptime(selected_date, '%Y-%m-%d').date()
            events = Event.objects.filter(user=request.user, date=selected_date)
        else:
            events = Event.objects.filter(user=request.user, date=timezone.now().date())
        return render(request, 'calendar.html',
                      {'tasks': tasks, 'completed_tasks_count': completed_tasks_count, 'events': events})

    except Exception as e:
        logger.error(e)
        return render(request, 'calendar.html',
                      {'tasks': tasks, 'completed_tasks_count': completed_tasks_count, 'events': events})


@custom_login_required
def add_task(request):
    try:
        if request.method == 'POST':
            form = TaskForm(request.POST)
            if form.is_valid():
                task = form.save(commit=False)
                task.user = request.user
                task.save()
                return redirect('calendar')
        else:
            form = TaskForm()
        return render(request, 'calendar/add_task.html', {'form': form})
    except Exception as e:
        logger.error(e)
        return render(request, 'calendar/add_task.html', {'form': form})


@login_required
def complete_task(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
        if task.completed:
            task.completed = False
        else:
            task.completed = True
        task.save()
        return redirect('calendar')

    except Exception as e:
        logger.error(e)
        return redirect('calendar')


@custom_login_required
def delete_task(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
        task.delete()
        return redirect('calendar')

    except Exception as e:
        logger.error(e)
        return redirect('calendar')
