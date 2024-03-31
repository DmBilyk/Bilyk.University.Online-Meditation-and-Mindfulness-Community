from django.contrib.auth.models import User
from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils import timezone


#Profile model for creating
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    google_email = models.EmailField()
    google_name = models.CharField(max_length=255)
    events = models.TextField(default="")

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    google_id = models.CharField(max_length=255, unique=True, null=True, blank=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    country_choices = [
        ('US', 'United States'),
        ('UK', 'United Kingdom'),
        ('CA', 'Canada'),
    ]
    level_choices = [
        ('BEG', 'Beginner'),
        ('INT', 'Intermediate'),
        ('PRO', 'Professional'),
    ]
    level = models.CharField(max_length=3, choices=level_choices, blank=True, null=True)
    country = models.CharField(max_length=2, choices=country_choices, blank=True, null=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username


class PersonalCalendar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_title = models.CharField(max_length=255)
    event_description = models.TextField()
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    location = models.CharField(max_length=255, blank=True, null=True)
    reminder = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.event_title


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.TimeField(default=timezone.now().time())
    description = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    last_reset = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.description


from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.URLField(default='', blank=True)
    youtube_link = models.URLField(default='')

    def __str__(self):
        return self.title
