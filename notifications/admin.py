# notifications/admin.py
from django.contrib import admin
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from .models import Notification, NotificationTemplate

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('message_type', 'get_users', 'is_sent')
    actions = ['send_notifications']

    def get_users(self, obj):
        return ", ".join([user.username for user in obj.users.all()])
    get_users.short_description = 'Users'

    def send_notifications(self, request, queryset):
        for notification in queryset:
            if not notification.is_sent:
                template_name = f'notifications/{notification.message_type}.html'
                context = {'message': notification.message}
                html_message = render_to_string(template_name, context)
                for user in notification.users.all():
                    send_mail(
                        subject=notification.message_type,
                        message='',
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=[user.email],
                        html_message=html_message,
                    )
                notification.is_sent = True
                notification.save()
        self.message_user(request, "Notifications sent successfully.")
    send_notifications.short_description = "Send selected notifications"

admin.site.register(Notification, NotificationAdmin)
admin.site.register(NotificationTemplate)