from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def books_searching(request):
    return render(request, 'books_searching.html')

def borrowed_books(request):
    return render(request, 'borrowed_books.html')

def reading_book(request):
    return render(request, 'reading_book.html')

def login(request):
    return render(request, 'login.html')

def registration(request):
    return render(request, 'registration.html')