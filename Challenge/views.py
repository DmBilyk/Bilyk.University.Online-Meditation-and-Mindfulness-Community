from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from WEB.decorators import custom_login_required
from .models import WeeklyChallenge, UserChallenge, DayTask
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@custom_login_required
def challenge_list(request):
    try:
        challenges = WeeklyChallenge.objects.all()
        return render(request, 'challenges/challenge_list.html', {'challenges': challenges})
    except Exception as e:
        logger.error(e)
        return render(request, 'challenges/challenge_list.html', {'challenges': []})


def join_challenge(request, challenge_id):
    try:
        challenge = get_object_or_404(WeeklyChallenge, id=challenge_id)
        user_challenge, created = UserChallenge.objects.get_or_create(user=request.user, challenge=challenge)

        if not created and user_challenge.is_joined:
            return redirect('challenge_detail', challenge_id=challenge.id)

        user_challenge.is_joined = True
        user_challenge.save()

        return redirect('challenge_detail', challenge_id=challenge.id)
    except Exception as e:
        logger.error(e)
        return redirect('challenge_list')


def challenge_detail(request, challenge_id):
    try:
        challenge = get_object_or_404(WeeklyChallenge, id=challenge_id)
        user_challenge = get_object_or_404(UserChallenge, user=request.user, challenge=challenge)

        time_difference = timezone.now() - user_challenge.join_date
        current_day = time_difference.days + 1

        current_day_tasks = challenge.tasks.filter(day_number=current_day)

        successful_days = user_challenge.completed_tasks.count()

        return render(request, 'challenges/challenge_detail.html',
                      {'challenge': challenge, 'user_challenge': user_challenge, 'current_day_tasks': current_day_tasks,
                       'successful_days': successful_days})
    except Exception as e:
        logger.error(e)
        return redirect('challenge_list')
