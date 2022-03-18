""" Urls for Profiles app """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
]
