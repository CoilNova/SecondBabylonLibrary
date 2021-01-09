from django.shortcuts import render, redirect
from .models import Book, ReadingList, CompleteList
from django.http import HttpResponseRedirect

def Reading(request):
    if request.user.is_authenticated:
        current_user = request.user
        reading = ReadingList.objects.all().filter(user_id=current_user)

        return render(request, 'Books/main.html', {'reading': reading})

    else:
        return HttpResponseRedirect("/login")

def Searching(request):
    if request.user.is_authenticated:
        current_user = request.user
        books = Book.objects.all()
        reading = ReadingList.objects.all().filter(user_id=current_user)
        array = []
        for r in reading:
            array.append(r.book_id)
        complete = CompleteList.objects.all().filter(user_id=current_user)
        return render(request, 'Books/search.html', {'array': array, 'complete': complete, 'books':books})
    else:
        return HttpResponseRedirect("/login")

def create(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            newbook = ReadingList()
            newbook.user_id = request.user
            book_id = request.POST.get("book_id")
            book = Book.objects.get(id=book_id)
            book.count = book.count - 1
            newbook.book_id = book
            newbook.days = 15
            newbook.save()
            book.save()
        return HttpResponseRedirect("/main/")

def delete(request, id):
    if request.user.is_authenticated:
        try:
            reading = ReadingList.objects.get(id=id)
            book = Book.objects.get(id=reading.book_id.id)
            book.count = book.count+1
            book.save()
            reading.delete()
            return HttpResponseRedirect("/search")
        except Person.DoesNotExist:
            return HttpResponseNotFound("<h2>Book not found</h2>")