from django.http import HttpResponse
from django.shortcuts import render ,redirect
from WEB.models import UserProfile
from .forms import ProfileForm
from .models import Profile
from django.contrib.auth.decorators import login_required

def home (request):
    return render(request, 'home.html', {'user': request.user})


def profile_view(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    print("User profile:", user_profile)
    return render(request, 'profile.html', {'user_profile': user_profile})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile.html')  # Замініть 'profile' на URL вашої сторінки профілю
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'edit_profile.html', {'form': form})