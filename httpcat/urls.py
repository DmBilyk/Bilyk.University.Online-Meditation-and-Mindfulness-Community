from django.urls import path
from .views import HttpCatView

urlpatterns = [
    path('httpcat/<int:status_code>/', HttpCatView.as_view(), name='httpcat'),
]