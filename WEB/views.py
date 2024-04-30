import logging
from django.shortcuts import redirect
from .decorators import custom_login_required
from WEB.models import UserProfile
from .forms import ProfileForm
from .models import Profile
from django.shortcuts import render, get_object_or_404
import re
from .models import Video_Youtube
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def faq(request):
    return render(request, 'faq.html')


def home(request):
    return render(request, 'home.html', {'user': request.user})


@custom_login_required
def profile_view(request):
    try:
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)
        logger.info("User profile: %s", user_profile)
        return render(request, 'profile.html', {'user_profile': user_profile})
    except Exception as e:
        logger.exception("Error in profile_view: %s", e)
        raise


@custom_login_required
def edit_profile(request):
    user = request.user
    try:
        profile = user.profile
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'edit_profile.html', {'form': form})


def get_list_video(request):
    videos = Video_Youtube.objects.all()
    return render(request, 'video/video_list.html', {'video_list': videos})


def extract_video_id(url):
    video_id = None
    match = re.search(r"(?<=v=)[a-zA-Z0-9_-]+", url)
    if match:
        video_id = match.group(0)
    return video_id


def get_video_id(youtube_link):
    return extract_video_id(youtube_link)


def get_video(request, pk: int):
    video = get_object_or_404(Video_Youtube, id=pk)
    video_id = get_video_id(video.youtube_link)
    return render(request, "video/video.html", {"video": video, "video_id": video_id})
