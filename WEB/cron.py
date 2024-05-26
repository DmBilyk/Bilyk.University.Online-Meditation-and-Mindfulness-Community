from django_cron import CronJobBase, Schedule
from Progress.models import Event
from django.utils import timezone
from datetime import datetime, timedelta
from Progress.views import send_event_notification

import logging
from django.utils import timezone


class EventNotificationCronJob(CronJobBase):
    RUN_EVERY_MINS = 10

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'event_notification_cron_job'

    def do(self):
        current_datetime = timezone.now()
        events = Event.objects.filter(date=current_datetime.date(), time__gte=current_datetime.time())

        logging.info(f'Found {len(events)} events to notify.')

        for event in events:
            event_datetime = datetime.combine(current_datetime.date(), event.time)
            notification_time = event_datetime - timedelta(hours=1)
            logging.info(f'Sending notification for event {event.id} to user {event.user_id} at {notification_time}.')
            send_event_notification(event.user_id, event, notification_time)
