from django.db import models


class Author(models.Model):
    DEFAULT_NAME = 'Unknown'

    name = models.CharField(max_length=100, verbose_name='Author Name', default=DEFAULT_NAME)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Category Name')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Book(models.Model):
    COVER_TYPE_CHOICES = [
        ('hardback', 'Hardback'),
        ('paperback', 'Paperback'),
        ('special', 'Special'),
    ]

    name = models.CharField(max_length=100, verbose_name='Title')
    page_count = models.IntegerField(verbose_name='Page Count')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price')
    image = models.ImageField(upload_to='book_images/', null=True, blank=True, verbose_name='Image')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books', verbose_name='Author')
    cover_type = models.CharField(max_length=20, choices=COVER_TYPE_CHOICES, default='hardback',
                                  verbose_name='Cover Type')
    categories = models.ManyToManyField(Category, related_name='books', verbose_name='Categories')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
