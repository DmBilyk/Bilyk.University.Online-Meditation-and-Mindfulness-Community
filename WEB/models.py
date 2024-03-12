from django.contrib.auth.models import User
from django.db import models

#Profile model for creating
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    google_email = models.EmailField()
    google_name = models.CharField(max_length=255)



#Profile model for editing
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    google_id = models.CharField(max_length=255, unique=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    country_choices = [
        ('US', 'United States'),
        ('UK', 'United Kingdom'),
        ('CA', 'Canada'),

    ]
    level_choise = [
        ('Beginner'),
        ('Intermediate'),
        ('Professional'),

    ]
    level = models.CharField(max_length=2, choices=level_choise, blank=True, null=True)
    country = models.CharField(max_length=2, choices=country_choices, blank=True, null=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username