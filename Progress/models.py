from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from WEB.models import User


class TaskCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    color = models.CharField(max_length=7, default='#007bff')  # Default color blue

    def __str__(self):
        return self.name


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.TimeField(default=timezone.now().time())
    description = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    last_reset = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(TaskCategory, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.description
