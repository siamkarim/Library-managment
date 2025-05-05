#make url patterns for books
from django.urls import path
from django.urls import re_path
from django.urls import include
from .views import BookListView, BookDetailView, AuthorListView, AuthorDetailView


urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('authors/', AuthorListView.as_view(), name='author-list'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
 
]