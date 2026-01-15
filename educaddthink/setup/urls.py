from django.urls import path
from .views import setup_master

urlpatterns = [
    path('setup/', setup_master, name='setup_master'),
]
