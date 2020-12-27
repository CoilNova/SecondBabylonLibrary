from django.contrib import admin
from .models import Book, ReadingList, CompleteList

admin.site.register(Book)
admin.site.register(ReadingList)
admin.site.register(CompleteList)
