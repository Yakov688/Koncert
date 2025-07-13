# authors = Author.objects.filter(first_name='John')
# authors = Author.objects.exclude(last_name='Doe')

# books = Book.objects.filter(price__lt=500)
# books = Book.objects.filter(price__lte=300)

# books = Book.objects.filter(price__gt=1000)
# books = Book.objects.filter(price__gte=750)

# books = Book.objects.filter(title__contains='django')
# books = Book.objects.filter(title__icontains='python')
# books = Book.objects.filter(title__startswith='Advanced')
# books = Book.objects.filter(title__istartswith='pro')
# books = Book.objects.filter(title__endswith='Guide')
# books = Book.objects.filter(title__iendswith='tutorial')

# reviews = Review.objects.filter(comment__isnull=True)
# reviews = Review.objects.filter(comment__isnull=False)

# authors = Author.objects.filter(id__in(1, 3, 5))
# books = Book.objects.filter(Q(published_date__gt=datetime(2023, 1, 1)) & Q(published_date__lt=datetime(2023, 12, 31)))

# books = Book.objects.filter(title__startswith='Python')
# authors = Author.objects.filter(last_name__istartswith='Mc')

# books = Book.objects.filter(published_date__year=2024)
# books = Book.objects.filter(published_date__month=6)
# reviews = Review.objects.filter(created_at__day=11)
# reviews = Review.objects.filter(created_at__week_day=2)
# books = Book.objects.filter(Q(published_date__gt=datetime(2025, 4, 1)) & Q(published_date__lt=datetime(2025, 6, 30)))
# reviews = Review.objects.filter(created_at__date=date(2025, 7, 11))
# reviews = Review.objects.filter(Q(created_at__hour=15) & Q(created_at__minute=30) & Q(created_at__second=0))
# reviews = Review.objects.filter(created_at__hour=15)
# reviews = Review.objects.filter(created_at__minute=30)
# reviews = Review.objects.filter(created_at__second=0)


# books = Book.objects.filter(author__last_name__icontains='smith')
# books = Book.objects.filter(author__email='author@example.com')
# authors = Author.objects.annotate(books_count=Count('books')).filter(books_count__gt=5)


# books = Book.objects.filter(Q(metadata__genre='fiction'))
# books = Book.objects.filter(Q(metadata__tags__icontains='bestseller'))

# authors = Author.objects.filter(first_name='Alice').exclude(last_name='Brown')


# authors = Author.objects.annotate(books_count=Count('books'))
# books = Book.objects.annotate(avg_rating=Avg('reviews__rating'))
# books = Book.objects.annotate(total_price=ExpressionWrapper(F('price') - F('price') * F('discount') / 100,
#                                                                              output_field=DecimalField()))


# books = Book.objects.select_related('author').all()
# authors = Author.objects.prefetch_related('books').all()
