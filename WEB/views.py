from django.http import HttpResponse
from django.shortcuts import render ,redirect
from WEB.models import UserProfile
from .forms import ProfileForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile


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