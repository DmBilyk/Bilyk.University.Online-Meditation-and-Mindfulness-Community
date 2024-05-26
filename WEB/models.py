from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils import timezone


# Profile model for creating
class UserProfile(models.Model):
    """
    A class used to represent a User Profile

    Attributes
    ----------
    user : User
        a User object representing the user associated with the profile
    google_email : str
        a string representing the Google email of the user
    google_name : str
        a string representing the Google name of the user (max_length=255)
    events : str
        a string representing the events associated with the user
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    google_email = models.EmailField()
    google_name = models.CharField(max_length=255)
    events = models.TextField(default="")


# Profile model for custom
class Profile(models.Model):
    """
    A class used to represent a Profile

    Attributes
    ----------
    user : User
        a User object representing the user associated with the profile
    google_id : str
        a string representing the Google ID of the user (max_length=255)
    age : int
        an integer representing the age of the user
    country_choices : list
        a list of tuples representing the country choices for the user
    level_choices : list
        a list of tuples representing the level choices for the user
    level : str
        a string representing the level of the user (max_length=3)
    country : str
        a string representing the country of the user (max_length=2)
    bio : str
        a string representing the bio of the user
    """

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


class Video(models.Model):
    """
    A class used to represent a Video

    Attributes
    ----------
    title : str
        a string representing the title of the video (max_length=100)
    description : str
        a string representing the description of the video
    image : ImageField
        an ImageField representing the image of the video
    file : FileField
        a FileField representing the file of the video
    create_at : datetime
        a datetime representing the creation time of the video
    """

    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='image/')
    file = models.FileField(
        upload_to='video/',
        validators=[FileExtensionValidator(allowed_extensions=['mp4'])],
        default='default.mp4'
    )
    create_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Video_Youtube(models.Model):
    """
    A class used to represent a YouTube Video

    Attributes
    ----------
    title : str
        a string representing the title of the video (max_length=100)
    description : str
        a string representing the description of the video
    image_url : str
        a string representing the image URL of the video
    youtube_link : str
        a string representing the YouTube link of the video
    """

    title = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.URLField(default='', blank=True)
    youtube_link = models.URLField(default='')

    def __str__(self):
        return self.title
