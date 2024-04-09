from django.urls import path

from . import views

app_name = 'feedback'

urlpatterns = [
    path('feedback/', views.feedback_form, name='feedback_form'),
]
