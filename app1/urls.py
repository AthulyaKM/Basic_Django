from django import urls
from django.urls import path
from . import views
from .views import index

urlpatterns = [
    path('sample/', views.index),
    path('home/', views.home)
]
