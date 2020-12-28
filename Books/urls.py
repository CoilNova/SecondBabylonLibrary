from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Reading, name='main'),
    path('search/', views.Searching, name='search')
]