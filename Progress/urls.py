from django.urls import path
from .views import calendar_view, add_task, complete_task, delete_task

urlpatterns = [
    path('calendar/', calendar_view, name='calendar'),
    path('add_task/', add_task, name='add_task'),
    path('complete_task/<int:task_id>/', complete_task, name='complete_task'),
    path('delete_task/<int:task_id>/', delete_task, name='delete_task'),
]
