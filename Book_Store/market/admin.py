from django.contrib import admin
from .models import Book, Author, Category


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'page_count', 'price', 'cover_type')
    list_filter = ('author', 'categories', 'cover_type')
    search_fields = ('name', 'author__name')


admin.site.register(Author)
admin.site.register(Book, BookAdmin)
admin.site.register(Category)