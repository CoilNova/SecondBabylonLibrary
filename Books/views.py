from django.shortcuts import render
from .models import Book, ReadingList, CompleteList


def Reading(request):
    books = Book.objects.all()
    reading = ReadingList.objects.all()
    return render(request, 'Books/main.html', {'books': books, 'reading': reading})
