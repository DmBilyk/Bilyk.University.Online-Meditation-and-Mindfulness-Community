from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_page, name='chat_page'),
    path('get_openai_response/', views.get_openai_response, name='get_openai_response'),
]