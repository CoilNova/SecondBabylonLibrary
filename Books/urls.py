from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include, url

app_name = 'Books'
urlpatterns = [
    path('', views.Reading, name='main'),
    path('search/', views.Searching, name='search'),
    path('add/<int:rbookid>', views.AddReading, name ='addreading'),
    path('create/', views.create),
    path('delete/<int:id>', views.delete, name='delete'),
]