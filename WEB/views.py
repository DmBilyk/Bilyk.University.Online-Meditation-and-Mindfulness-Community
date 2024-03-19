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
    return render(request, 'video/video_list.html', {'video_list': Video.objects.all()})


def get_video(request, pk: int):
    _video = get_object_or_404(Video, id=pk)
    return render(request, "video/video.html", {"video": _video})


def get_streaming_video(request, pk: int):
    file, status_code, content_length, content_range = open_file(request, pk)
    response = StreamingHttpResponse(file, status=status_code, content_type='video/mp4')

    response['Accept-Ranges'] = 'bytes'
    response['Content-Length'] = str(content_length)
    response['Cache-Control'] = 'no-cache'
    response['Content-Range'] = content_range
    return response