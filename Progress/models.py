from django.db import models
from django.utils import timezone
from WEB.models import User


class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    time = models.TimeField()
    date = models.DateField()
    link = models.URLField()

    def __str__(self):
        return self.name


class TaskCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    color = models.CharField(max_length=7, default='#003bff')

    def __str__(self):
        return self.name


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.TimeField(default=timezone.now)
    description = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    last_reset = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(TaskCategory, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.description
