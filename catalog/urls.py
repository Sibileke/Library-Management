from django.contrib import admin
from django.urls import path, include

from .views import author_list, genre_list, genre_details, book_list, book_details, author_list, author_details, book_instance_details, book_instance_list

urlpatterns = [
    path('genres/', genre_list),
    path('genre/<int:id>', genre_details),
    path('books/', book_list),
    path('book/<int:id>', book_details),
    path('authors/', author_list),
    path('author/<int:id>', author_details),
    path('book_instance/', book_instance_list),
    path('book_instance/<int:id>', book_instance_details),
]