from django.http import HttpResponse
from django.shortcuts import render
from WEB.models import UserProfile

def home (request):
    return render(request, 'home.html', {'user': request.user})


def profile_view(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    print("User profile:", user_profile)
    return render(request, 'profile.html', {'user_profile': user_profile})