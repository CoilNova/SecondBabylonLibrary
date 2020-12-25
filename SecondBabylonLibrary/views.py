from django.shortcuts import render

def index(request):
    return render(request, 'login.html')

def registration(request):
    return render(request, 'registration.html')