import logging
import re
from django.dispatch import receiver
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from rest_framework.decorators import api_view
from django.contrib.auth.signals import user_logged_in
from WEB.models import UserProfile
from .decorators import custom_login_required
from .forms import ProfileForm
from .models import Profile
from .models import Video_Youtube
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required


# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)












@api_view(['GET'])
def about(request):
    """
    Handles the about page request.
    """
    return render(request, 'about.html')



@api_view(['GET'])
def faq(request):
    """
    Handles the FAQ page request.
    """
    return render(request, 'faq.html')


@api_view(['GET'])
def home(request):
    """
    Handles the home page request.
    """
    return render(request, 'home.html', {'user': request.user})


@api_view(['GET'])
@custom_login_required
def profile_view(request):
    """
    Handles the profile view request.
    """
    try:
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)
        logger.info("User profile: %s", user_profile)
        return render(request, 'profile.html', {'user_profile': user_profile})
    except Exception as e:
        logger.exception("Error in profile_view: %s", e)
        raise



@custom_login_required
def edit_profile(request):
    """
    Handles the edit profile request.
    """
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


@api_view(['GET'])
def get_list_video(request):
    """
    Handles the video list request.
    """
    videos = Video_Youtube.objects.all()
    return render(request, 'video/video_list.html', {'video_list': videos})


def extract_video_id(url):
    """
    Extracts the video ID from a YouTube URL.
    """
    video_id = None
    match = re.search(r"(?<=v=)[a-zA-Z0-9_-]+", url)
    if match:
        video_id = match.group(0)
    return video_id


def get_video_id(youtube_link):
    """
    Returns the video ID from a YouTube link.
    """
    return extract_video_id(youtube_link)


@api_view(['GET'])
def get_video(request, pk: int):
    """
    Handles the video request.
    """
    video = get_object_or_404(Video_Youtube, id=pk)
    video_id = get_video_id(video.youtube_link)
    return render(request, "video/video.html", {"video": video, "video_id": video_id})


@login_required
def send_email(request, subject, message, user_email=None):
    user = request.user
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [user.email]
    if user_email:
        recipient_list[0] = user_email
    send_mail(subject, message, from_email, recipient_list, fail_silently=False)
    return redirect('home')


@receiver(user_logged_in)
def send_welcome_email_if_google_auth(sender, request, user, **kwargs):
    if user.socialaccount_set.filter(provider='google').exists():
        if not hasattr(user, '_welcome_email_sent'):
            subject = 'Welcome to Calm-Connections!'
            message = f'Hello {user.username}, thanks for joining our community!'
            send_email(request, subject, message)
            user._welcome_email_sent = True
