from django.urls import path
from . import views

urlpatterns = [
    path('', views.forum_index, name='forum_index'),
    path('create/', views.create_post, name='create_post'),

]
