from django.contrib import admin
from .models import Author, BookInstance, Book, Genre

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookInstance)
admin.site.register(Genre)
