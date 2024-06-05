from django.views import View
from django.shortcuts import render, redirect
from .models import Notification, NotificationTemplate
from .forms import NotificationForm

class SendNotificationView(View):
    def get(self, request):
        form = NotificationForm()
        return render(request, 'notifications/send_notification.html', {'form': form})

    def post(self, request):
        form = NotificationForm(request.POST)
        if form.is_valid():
            notification = form.save(commit=False)
            notification_template = NotificationTemplate.objects.get(message_type=notification.message_type)
            notification.is_sent = True
            notification.save()
        return redirect('admin')