import logging
from django.shortcuts import redirect
from .decorators import custom_login_required
from WEB.models import UserProfile
from .forms import ProfileForm
from .models import Profile
from django.http import StreamingHttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Video
from .services import open_file
import re
from django.http import HttpResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .models import Video_Youtube


def test_media_storage(request):
    # Create a simple text file content
    file_content = ContentFile("Hello, World!".encode())

    # Save the file to media storage
    file_name = default_storage.save('test.txt', file_content)

    # Try to open the file from media storage
    with default_storage.open(file_name) as f:
        file_data = f.read()

    # Delete the test file
    default_storage.delete(file_name)

    # Return the file data in the response
    return HttpResponse(file_data)


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
