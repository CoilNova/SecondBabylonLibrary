from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=50, help_text="Название книги")
    author = models.CharField(max_length=50, help_text="Автор книги")
    cover = models.ImageField(upload_to='covers')
    count = models.IntegerField()


class ReadingList(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    days = models.IntegerField()


class CompleteList(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
