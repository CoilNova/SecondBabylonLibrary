from django.shortcuts import render
from .models import Book, ReadingList, CompleteList


def Reading(request):
    books = Book.objects.all()
    reading = ReadingList.objects.all()
    return render(request, 'Books/main.html', {'books': books, 'reading': reading})

def Searching(request):
    current_user_id = request.user.id
    books = Book.objects.all()
    reading = ReadingList.objects.all().filter(user_id=current_user_id)
    complete = CompleteList.objects.all().filter(user_id=current_user_id)
    return render(request, 'Books/search.html', {'books': books, 'reading': reading, 'complete': complete})
