from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
from WEB.models import UserProfile


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            if request.user.is_authenticated:
                user_profile = UserProfile.objects.get(user=request.user)

                post.user = request.user
                post.user_name = user_profile.google_name
                post.save()
                return redirect('forum_index')
            else:
                return redirect('/')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})


def forum_index(request):
    posts = Post.objects.all()
    return render(request, 'forum_index.html', {'posts': posts})
