from django.shortcuts import render, redirect
from .models import Book, ReadingList, CompleteList


def Reading(request):
    current_user = request.user
    reading = ReadingList.objects.all().filter(user_id=current_user)
    return render(request, 'Books/main.html', {'reading': reading})

def Searching(request):
    current_user = request.user
    books = Book.objects.all()
    reading = ReadingList.objects.all().filter(user_id=current_user)
    complete = CompleteList.objects.all().filter(user_id=current_user)
    return render(request, 'Books/search.html', {'reading': reading, 'complete': complete, 'books':books})

def AddReading(request, rbookid):
    reading = ReadingList()
    reading.user_id = request.user
    reading.book_id = Book.objects.get(pk=rbookid)
    reading.save
    return redirect(request, '/login')
