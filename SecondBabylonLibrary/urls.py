"""SecondBabylonLibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books_searching', views.books_searching),
    path('borrowed_books', views.borrowed_books),
    path('reading_book', views.reading_book),
    url(r'^login/$', views.LoginFormView.as_view(), name='login'),
    url(r'^signup/$', views.RegisterFormView.as_view(), name='signup'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url('main/', include('Books.urls')),
    url('search/', include('Books.urls')),
    path('read/<int:rbookid>', views.read, name = "read"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
