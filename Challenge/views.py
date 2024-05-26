from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import WeeklyChallenge, UserChallenge, DayTask


def challenge_list(request):
    """
    Handles the challenge list request.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    """

    challenges = WeeklyChallenge.objects.all()
    return render(request, 'challenges/challenge_list.html', {'challenges': challenges})


def join_challenge(request, challenge_id):
    """
    Handles the request to join a challenge.

    Args:
        request (HttpRequest): The request object.
        challenge_id (int): The ID of the challenge to join.

    Returns:
        HttpResponse: The response object.
    """

    challenge = get_object_or_404(WeeklyChallenge, id=challenge_id)
    user_challenge, created = UserChallenge.objects.get_or_create(user=request.user, challenge=challenge)

    if not created and user_challenge.is_joined:
        return redirect('challenge_detail', challenge_id=challenge.id)

    user_challenge.is_joined = True
    user_challenge.save()

    return redirect('challenge_detail', challenge_id=challenge.id)


def challenge_detail(request, challenge_id):
    """
    Handles the challenge detail request.

    Args:
        request (HttpRequest): The request object.
        challenge_id (int): The ID of the challenge to view.

    Returns:
        HttpResponse: The response object.
    """

    challenge = get_object_or_404(WeeklyChallenge, id=challenge_id)
    user_challenge = get_object_or_404(UserChallenge, user=request.user, challenge=challenge)

    time_difference = timezone.now() - user_challenge.join_date
    current_day = time_difference.days + 1

    current_day_tasks = challenge.tasks.filter(day_number=current_day)

    if request.method == 'POST':
        selected_tasks = request.POST.getlist('tasks')
        user_challenge.completed_tasks.clear()
        for task_id in selected_tasks:
            task = get_object_or_404(DayTask, id=task_id)
            user_challenge.completed_tasks.add(task)

    successful_days = user_challenge.completed_tasks.count()

    return render(request, 'challenges/challenge_detail.html',
                  {'challenge': challenge, 'user_challenge': user_challenge, 'current_day_tasks': current_day_tasks,
                   'successful_days': successful_days})
