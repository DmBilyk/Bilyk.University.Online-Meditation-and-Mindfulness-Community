from django.urls import path
from . import views

urlpatterns = [
    path('issues/', views.get_github_issues, name='issues_list'),
]

