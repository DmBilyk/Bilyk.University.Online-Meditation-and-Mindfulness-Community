from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):
    MESSAGE_TYPES = (
        ('long_time_no_see', 'You haven\'t visited us for a long time'),
        ('new_feature', 'We have a new feature out, try it'),
        ('new_challenge', 'We have a new unique weekly challenge, join us'),
    )
    message_type = models.CharField(max_length=20, choices=MESSAGE_TYPES)
    users = models.ManyToManyField(User)
    message = models.TextField()
    is_sent = models.BooleanField(default=False)



class NotificationTemplate(models.Model):
    message_type = models.CharField(max_length=20, choices=Notification.MESSAGE_TYPES)
    template = models.TextField()

    def __str__(self):
        return self.message_type

