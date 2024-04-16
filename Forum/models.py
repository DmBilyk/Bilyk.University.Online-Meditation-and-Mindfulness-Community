from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post by {self.user.username}"


class Response(models.Model):
    parent_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='responses')
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    reply_to = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return f"Response to {self.parent_post}"
