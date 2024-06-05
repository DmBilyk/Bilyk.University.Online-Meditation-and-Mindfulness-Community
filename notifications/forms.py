# notifications/forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Notification

class NotificationForm(forms.ModelForm):
    users = forms.ModelMultipleChoiceField(queryset=User.objects.all())

    class Meta:
        model = Notification
        fields = ['message_type', 'users', 'message']