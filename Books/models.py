from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=50, help_text="Название книги")
    author = models.CharField(max_length=50, help_text="Автор книги")
    cover = models.ImageField(upload_to='covers')
    date = models.DateField()
    count = models.IntegerField()


class ReadingList(models.Model):
    user_id = models.IntegerField()
    book_id = models.IntegerField()


class CompleteList(models.Model):
    user_id = models.IntegerField()
    book_id = models.IntegerField()
