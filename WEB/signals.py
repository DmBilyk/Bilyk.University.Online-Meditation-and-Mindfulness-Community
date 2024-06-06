from allauth.account.signals import user_signed_up
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in
from .views import send_email

from .models import UserProfile


from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

@receiver(user_signed_up)
def save_profile_data(request, user, **kwargs):
    if user and kwargs.get('sociallogin'):
        if kwargs['sociallogin'].account.provider == 'google':
            google_email = kwargs['sociallogin'].account.extra_data.get('email')
            google_name = kwargs['sociallogin'].account.extra_data.get('name')
            UserProfile.objects.create(user=user, google_email=google_email, google_name=google_name)

            # Prepare email content
            subject = 'Welcome to our community!'
            message = render_to_string('email/welcome_email.html', {'name': google_name})
            from_email = settings.EMAIL_HOST_USER
            to_email = [google_email]
            print(to_email)

            # Send email
            send_mail(subject, '', from_email, to_email, html_message=message)


@receiver(post_save, sender=UserProfile)
def update_user_profile(sender, instance, created, **kwargs):
    if not created:
        instance.user.google_email = instance.google_email
        instance.user.google_name = instance.google_name
        instance.user.save()




@receiver(post_save, sender=User)
def check_new_user(sender, instance, created, **kwargs):
    if created:
        instance._newly_created = True
    elif not hasattr(instance, '_newly_created'):
        instance._newly_created = False


@receiver(user_logged_in)
def send_welcome_email_if_new(sender, request, user, **kwargs):
    if (getattr(user, '_newly_created') and
            user.backend == 'allauth.account.auth_backends.AuthenticationBackend'):
        subject = 'Welcome to Calm-Connections!'
        message = f'{user.username}, thanks for becoming a part of our community!'
        send_email(request, subject, message)
