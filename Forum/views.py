import logging

from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from WEB.decorators import custom_login_required
from .forms import PostForm
from .models import Post, Response

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@custom_login_required
def forum_index(request):
    """
    Handles the forum index request.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    """

    try:
        posts_with_responses = [{'post': post, 'responses': post.responses.all()} for post in Post.objects.all()]
        return render(request, 'forum_index.html', {'posts_with_responses': posts_with_responses})
    except Exception as e:
        logger.error(e)
        return redirect('forum_index')


@custom_login_required
def create_post(request):
    """
    Handles the request to create a new post.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    """

    try:
        form = PostForm(request.POST or None)
        if form.is_valid():
            new_post = Post(user=request.user, message=form.cleaned_data['message'])
            parent_post_id = request.GET.get('parent_post_id')
            if parent_post_id:
                new_post.parent_post = Post.objects.get(pk=parent_post_id)
            new_post.save()
            return redirect('forum_index')
        return render(request, 'create_post.html', {'form': form, 'parent_post_id': request.GET.get('parent_post_id')})
    except Exception as e:
        logger.error(e)
        return redirect('forum_index')


@custom_login_required
def reply_post(request, post_id):
    """
    Handles the request to reply to a post.

    Args:
        request (HttpRequest): The request object.
        post_id (int): The ID of the post to reply to.

    Returns:
        HttpResponse: The response object.
    """
    try:
        form = PostForm(request.POST or None)
        if form.is_valid():
            reply_to_id = request.POST.get('reply_to_id')
            reply_to = User.objects.get(pk=reply_to_id) if reply_to_id else None
            Response(parent_post=Post.objects.get(pk=post_id), message=form.cleaned_data['message'],
                     reply_to=reply_to).save()
            return redirect('forum_index')
        return render(request, 'reply_post.html', {'form': form, 'parent_post': Post.objects.get(pk=post_id)})
    except Exception as e:
        logger.error(e)
        return redirect('forum_index')
