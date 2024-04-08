from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models

class WeeklyChallenge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Weekly Challenge for {self.user.username}"


class Task(models.Model):
    challenge = models.ForeignKey(WeeklyChallenge, on_delete=models.CASCADE, related_name='tasks')
    day_number = models.PositiveIntegerField()
    description = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Day {self.day_number} Task for {self.challenge.user.username}"
