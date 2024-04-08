from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Task
from .forms import TaskForm
from django.contrib import messages
from django.db.models import Q


@login_required
def calendar_view(request):
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

    return render(request, 'calendar.html', {'tasks': tasks, 'completed_tasks_count': completed_tasks_count})


@login_required
def add_task(request):
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

@login_required
def complete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    if task.completed:
        task.completed = False
    else:
        task.completed = True
    task.save()
    return redirect('calendar')


@login_required
def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return redirect('calendar')
