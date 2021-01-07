from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from . import views


app_name = 'Books'
urlpatterns = [
    path('', views.Reading, name='main'),
    path('search/', views.Searching, name='search'),
    path('add/<int:rbookid>', views.AddReading, name ='addreading')
]