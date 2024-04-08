from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import WeeklyChallenge, Task
from .forms import TaskForm, WeeklyChallengeForm
from django.contrib import messages


@login_required
def calendar_view(request):
    today = timezone.now().date()
    user = request.user

    # Check if there is an ongoing weekly challenge for the user
    current_weekly_challenge = WeeklyChallenge.objects.filter(user=user, end_date__gte=timezone.now()).first()

    if current_weekly_challenge:
        tasks = Task.objects.filter(challenge=current_weekly_challenge)
        completed_tasks_count = tasks.filter(completed=True).count()
        progress_percentage = (completed_tasks_count / 7) * 100

        # Check if the user has completed 70% or more of the weekly challenge
        if progress_percentage >= 70:
            current_weekly_challenge.completed = True
            current_weekly_challenge.save()
            messages.success(request,
                             f'Congratulations! You have completed weekly challenge number {current_weekly_challenge.id}')
    else:
        # If there is no ongoing weekly challenge, display tasks for the current day
        tasks = Task.objects.filter(user=user, day_number=today.weekday() + 1)

    # Fetch overdue tasks for the user
    overdue_tasks = Task.objects.filter(user=user, completed=False, day_number__lt=today.weekday() + 1)

    # Notify the user about overdue tasks
    for task in overdue_tasks:
        messages.warning(request, f'Task "{task.description}" is overdue.')

    # Reset completed tasks if it has been more than 24 hours since the last reset
    first_task = user.task_set.first()
    if first_task is not None:
        last_reset_time = first_task.last_reset
        if timezone.now() - last_reset_time > timezone.timedelta(hours=24):
            Task.objects.filter(user=user).update(completed=False, last_reset=timezone.now())

    context = {
        'tasks': tasks,
        'completed_tasks_count': completed_tasks_count if current_weekly_challenge else Task.objects.filter(user=user,
                                                                                                            completed=True).count(),
        'progress_percentage': progress_percentage if current_weekly_challenge else None,
    }

    return render(request, 'calendar.html', context)


def join_weekly_challenge(request):
    if request.method == 'POST':
        form = WeeklyChallengeForm(request.POST)
        if form.is_valid():
            weekly_challenge = form.save(commit=False)
            weekly_challenge.user = request.user
            weekly_challenge.save()
            return redirect('calendar')  # Redirect to calendar or any other page
    else:
        form = WeeklyChallengeForm()
    return render(request, 'join_weekly_challenge.html', {'form': form})


@login_required
def create_weekly_challenge(request):
    if request.method == 'POST':
        # Process form submission
        form = WeeklyChallengeForm(request.POST)
        if form.is_valid():
            weekly_challenge = form.save(commit=False)
            weekly_challenge.user = request.user
            weekly_challenge.save()
            return redirect('calendar')  # Assuming you have a URL named 'calendar'
    else:
        # Display form for creating a new weekly challenge
        form = WeeklyChallengeForm()
    retu54
