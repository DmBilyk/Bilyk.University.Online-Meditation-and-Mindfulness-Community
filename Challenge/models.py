from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class DayTask(models.Model):
    """
    A class used to represent a Day Task

    Attributes
    ----------
    title : str
        a string representing the title of the task (max_length=255)
    description : str
        a string representing the description of the task
    day_number : int
        an integer representing the day number of the task
    """

    title = models.CharField(max_length=255)
    description = models.TextField()
    day_number = models.IntegerField()

    def __str__(self):
        return self.title


class WeeklyChallenge(models.Model):
    """
    A class used to represent a Weekly Challenge

    Attributes
    ----------
    title : str
        a string representing the title of the challenge (max_length=255)
    start_date : datetime
        a datetime representing the start date of the challenge
    end_date : datetime
        a datetime representing the end date of the challenge
    tasks : list
        a list of DayTask objects associated with the challenge
    """

    title = models.CharField(max_length=255)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField()
    tasks = models.ManyToManyField(DayTask)

    def __str__(self):
        return self.title


class UserChallenge(models.Model):
    """
    A class used to represent a User Challenge

    Attributes
    ----------
    user : User
        a User object representing the user associated with the challenge
    challenge : WeeklyChallenge
        a WeeklyChallenge object representing the challenge associated with the user
    completed_tasks : list
        a list of DayTask objects that the user has completed
    join_date : datetime
        a datetime representing the date the user joined the challenge
    is_joined : bool
        a boolean representing whether the user has joined the challenge
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    challenge = models.ForeignKey(WeeklyChallenge, on_delete=models.CASCADE)
    completed_tasks = models.ManyToManyField(DayTask)
    join_date = models.DateTimeField(default=timezone.now)
    is_joined = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        """
          Overrides the save method to set is_joined to True if the UserChallenge is being created for the first time.
          """
        if not self.pk:
            existing_challenge = UserChallenge.objects.filter(user=self.user, challenge=self.challenge)
            if not existing_challenge.exists():
                self.is_joined = True
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.challenge.title}"

    def is_completed(self):
        """
        Checks if the user has completed at least half of the tasks for the current day.

        Returns
        -------
        bool
            True if the user has completed at least half of the tasks for the current day, False otherwise
        """
        total_tasks_count = sum(
            task.day_number <= (timezone.now() - self.join_date).days + 1 for task in self.challenge.tasks.all())
        completed_tasks_count = self.completed_tasks.count()
        return total_tasks_count > 0 and completed_tasks_count >= total_tasks_count // 2
