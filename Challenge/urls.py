from django.urls import path

from . import views

urlpatterns = [
    path('challenges/', views.challenge_list, name='challenge_list'),
    path('challenges/join/<int:challenge_id>/', views.join_challenge, name='join_challenge'),
    path('challenges/<int:challenge_id>/', views.challenge_detail, name='challenge_detail'),
]
