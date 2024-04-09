from allauth.account.signals import user_signed_up
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import UserProfile


@receiver(user_signed_up)
def save_profile_data(request, user, **kwargs):
    if user and kwargs.get('sociallogin'):
        if kwargs['sociallogin'].account.provider == 'google':
            google_email = kwargs['sociallogin'].account.extra_data.get('email')
            google_name = kwargs['sociallogin'].account.extra_data.get('name')
            UserProfile.objects.create(user=user, google_email=google_email, google_name=google_name)


@receiver(post_save, sender=UserProfile)
def update_user_profile(sender, instance, created, **kwargs):
    if not created:
        instance.user.google_email = instance.google_email
        instance.user.google_name = instance.google_name
        instance.user.save()
