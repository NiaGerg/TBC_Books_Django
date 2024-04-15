from IPython.core.page import page
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from market.models import Book, Author


def get_books(request):
    books = Book.objects.order_by('name').values_list(
        'name', 'page_count', 'category', 'author_name', 'price', 'image__url')
    return_books = []
    for book in books:
        book_data = {
            'name': book[0],
            'page_count': book[1],
            'category': book[2],
            'author_name': book[3],
            'price': str(book[4]),
            'image_url': book[5] if book[5] else None,
        }
        return_books.append(book_data)
    return JsonResponse(return_books, safe=False)


def get_book(request, book_id):
    #book = Book.objects.all().get(pk=book_id)
    book = Book.objects.get(pk=book_id)
    return render(request, 'books/details.html', {'book': book})


def author_details(request, author_id):
    author = Author.objects.get(pk=author_id)
    books = author.books.all()
    return render(request, 'authors/details.html', {'author': author, 'books': books})


def index(request):
    page_size = 3
    name = request.GET.get('name', '')
    page_number = request.GET.get('page', 1)
    books_list = Book.objects.filter(name__icontains=name)

    paginator = Paginator(books_list, page_size)
    try:
        books = paginator.page(page_number)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'books': books})
