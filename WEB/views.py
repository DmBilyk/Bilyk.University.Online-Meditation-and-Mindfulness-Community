import re
import logging
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from .decorators import custom_login_required
from WEB.models import UserProfile
from .forms import ProfileForm
from .models import Profile
from .models import Video

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


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


@custom_login_required
def get_list_video(request):
    try:
        videos = Video.objects.all()
        return render(request, 'video/video_list.html', {'video_list': videos})
    except Exception as e:
        logger.exception("Error in get_list_video: %s", e)
        raise


def extract_video_id(url):
    try:
        video_id = url.split("v=")[1]
        ampersand_position = video_id.find("&")
        if ampersand_position != -1:
            video_id = video_id[:ampersand_position]
        return video_id
    except Exception as e:
        logger.exception("Error in extract_video_id: %s", e)
        return None

def get_video_id(youtube_link):
    return extract_video_id(youtube_link)


@custom_login_required
def get_video(request, pk: int):
    try:
        video = get_object_or_404(Video, id=pk)
        video_id = get_video_id(video.youtube_link)
        return render(request, "video/video.html", {"video": video, "video_id": video_id})
    except Exception as e:
        logger.exception("Error in get_video: %s", e)
        raise
