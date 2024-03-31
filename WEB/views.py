from django.http import HttpResponse
from django.shortcuts import render ,redirect
from WEB.models import UserProfile
from .forms import ProfileForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
from django.shortcuts import get_object_or_404
from django.http import StreamingHttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Video
from .services import open_file
import re

#main page
def home (request):
    return render(request, 'home.html', {'user': request.user})


#page profile
def profile_view(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    print("User profile:", user_profile)
    return render(request, 'profile.html', {'user_profile': user_profile})



#page edit-profile
@login_required
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
    videos = Video.objects.all()
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
    video = get_object_or_404(Video, id=pk)
    video_id = get_video_id(video.youtube_link)
    return render(request, "video/video.html", {"video": video, "video_id": video_id})
