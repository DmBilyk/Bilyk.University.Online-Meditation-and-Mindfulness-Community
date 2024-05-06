from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class DayTask(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    day_number = models.IntegerField()

    def __str__(self):
        return self.title


class WeeklyChallenge(models.Model):
    title = models.CharField(max_length=255)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField()
    tasks = models.ManyToManyField(DayTask)

    def __str__(self):
        return self.title


class UserChallenge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    challenge = models.ForeignKey(WeeklyChallenge, on_delete=models.CASCADE)
    completed_tasks = models.ManyToManyField(DayTask)
    join_date = models.DateTimeField(default=timezone.now)
    is_joined = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.pk:
            existing_challenge = UserChallenge.objects.filter(user=self.user, challenge=self.challenge)
            if not existing_challenge.exists():
                self.is_joined = True
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.challenge.title}"

    def is_completed(self):
        total_tasks_count = sum(
            task.day_number <= (timezone.now() - self.join_date).days + 1 for task in self.challenge.tasks.all())
        completed_tasks_count = self.completed_tasks.count()
        return total_tasks_count > 0 and completed_tasks_count >= total_tasks_count // 2
