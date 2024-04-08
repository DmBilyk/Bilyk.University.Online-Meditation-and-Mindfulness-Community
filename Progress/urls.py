from django.urls import path
from .views import calendar_view, add_task, complete_task, delete_task, join_weekly_challenge

urlpatterns = [
    path('calendar/', calendar_view, name='calendar'),
    path('add-task/', add_task, name='add_task'),
    path('complete-task/<int:task_id>/', complete_task, name='complete_task'),
    path('delete-task/<int:task_id>/', delete_task, name='delete_task'),
    path('join-weekly-challenge/', join_weekly_challenge, name='join_weekly_challenge'),
]
