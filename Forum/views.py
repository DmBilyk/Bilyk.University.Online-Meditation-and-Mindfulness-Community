from django.shortcuts import render, redirect

from .forms import PostForm
from .models import Post, Response


def forum_index(request):
    posts_with_responses = []
    posts = Post.objects.all()
    for post in posts:
        posts_with_responses.append({'post': post, 'responses': post.responses.all()})
    return render(request, 'forum_index.html', {'posts_with_responses': posts_with_responses})


def create_post(request):
    parent_post_id = request.GET.get('parent_post_id')
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            user = request.user
            message = form.cleaned_data['message']
            parent_post = None
            if parent_post_id:
                parent_post = Post.objects.get(pk=parent_post_id)
            new_post = Post(user=user, message=message)
            if parent_post:
                new_post.parent_post = parent_post
            new_post.save()
            return redirect('forum_index')
    else:
        form = PostForm()
    return render(request, 'forum/create_post.html', {'form': form, 'parent_post_id': parent_post_id})


def reply_post(request, post_id):
    parent_post = Post.objects.get(pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            user = request.user
            message = form.cleaned_data['message']
            new_response = Response(parent_post=parent_post, message=message)
            new_response.save()
            return redirect('forum_index')
    else:
        form = PostForm()
    return render(request, 'forum/reply_post.html', {'form': form, 'parent_post': parent_post})
