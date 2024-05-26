from django.urls import path

from .views import calendar_view, add_task, complete_task, delete_task, add_event, manage_events, edit_event, \
    delete_event

urlpatterns = [
    path('calendar/', calendar_view, name='calendar'),
    path('add_task/', add_task, name='add_task'),
    path('add_event/', add_event, name='add_event'),
    path('complete_task/<int:task_id>/', complete_task, name='complete_task'),
    path('delete_task/<int:task_id>/', delete_task, name='delete_task'),
    path('manage_events/', manage_events, name='manage_events'),
    path('edit_event/<int:event_id>/', edit_event, name='edit_event'),
    path('delete_event/<int:event_id>/', delete_event, name='delete_event'),
]
