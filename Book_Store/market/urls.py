from django.urls import path
from .views import get_books, get_book, index

urlpatterns = [
    path('books/', get_books, name='books'),
    path('books/<int:book_id>/', get_book, name='book'),
    path('', index, name='index'),
]