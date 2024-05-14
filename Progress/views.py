import logging
from datetime import datetime

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.db.models import Q
from django.http import HttpResponseServerError
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from WEB.decorators import custom_login_required
from WEB.models import User
from .forms import EventForm, TaskForm
from .models import Event
from .models import Task

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def send_event_notification(user_id, event, notification_time):
    """
    Sends an event notification email to the user.

    Args:
        user_id (int): The ID of the user to send the notification to.
        event (Event): The event to notify the user about.
        notification_time (datetime): The time to send the notification.
    """

    user = User.objects.get(id=user_id)

    recipient_email = user.email
    subject = f'Notification for event: {event.name}'
    body = f'Dear {user.username},\n\nYou have an upcoming event: {event.name} at {event.time} on {event.date}.\n\nDescription: {event.description}\n\nLink: {event.link}'

    if datetime.now() >= notification_time:
        try:
            send_mail(
                subject,
                body,
                settings.EMAIL_HOST_USER,
                [recipient_email],
                fail_silently=False,
            )
            print('Email sent successfully')
        except Exception as e:
            print(f'An error occurred while sending email: {e}')


@custom_login_required
def add_event(request):
    """
    Handles the request to add a new event.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    """

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
def edit_event(request, event_id):
    """
    Handles the request to edit an existing event.

    Args:
        request (HttpRequest): The request object.
        event_id (int): The ID of the event to edit.

    Returns:
        HttpResponse: The response object.
    """

    try:
        event = get_object_or_404(Event, pk=event_id, user=request.user)

        if request.method == 'POST':
            form = EventForm(request.POST, instance=event)
            if form.is_valid():
                form.save()
                return redirect('calendar')
        else:
            form = EventForm(instance=event)

        return render(request, 'calendar/edit_event.html', {'form': form, 'event': event})
    except Exception as e:
        logger.error(e)
        return HttpResponseServerError("An error occurred while processing your request.")


@custom_login_required
def manage_events(request):
    """
    Handles the request to manage events.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    """
    if request.method == 'POST':
        if 'delete' in request.POST:
            event_id = request.POST.get('delete')
            Event.objects.filter(id=event_id).delete()
            form = EventForm()
        elif 'edit' in request.POST:
            event_id = request.POST.get('edit')
            event = Event.objects.get(id=event_id)
            form = EventForm(instance=event)
        else:
            form = EventForm(request.POST)
            if form.is_valid():
                event_id = request.POST.get('event_id')
                event = Event.objects.get(id=event_id)
                form = EventForm(request.POST, instance=event)
                form.save()
    else:
        form = EventForm()

    events = Event.objects.filter(user=request.user)
    return render(request, 'calendar/manage_events.html', {'events': events, 'form': EventForm()})


@custom_login_required
def calendar_view(request):
    """
    Handles the request to view the calendar.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    """
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
    """
    Handles the request to add a new task.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    """

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
    """
    Handles the request to mark a task as complete.

    Args:
        request (HttpRequest): The request object.
        task_id (int): The ID of the task to mark as complete.

    Returns:
        HttpResponse: The response object.
    """
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
    """
    Handles the request to delete a task.

    Args:
        request (HttpRequest): The request object.
        task_id (int): The ID of the task to delete.

    Returns:
        HttpResponse: The response object.
    """

    try:
        task = Task.objects.get(pk=task_id)
        task.delete()
        return redirect('calendar')

    except Exception as e:
        logger.error(e)
        return redirect('calendar')


@custom_login_required
def delete_event(request, event_id):
    """
    Handles the request to delete an event.

    Args:
        request (HttpRequest): The request object.
        event_id (int): The ID of the event to delete.

    Returns:
        HttpResponse: The response object.
    """

    try:
        event = get_object_or_404(Event, id=event_id, user=request.user)

        event.delete()

        return redirect('manage_events')
    except Exception as e:
        logger.error(e)
        return redirect('manage_events')
