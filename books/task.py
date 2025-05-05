from celery import shared_task
from django.utils import timezone
from celery import shared_task
from .models import Book

#after 10 years books are archived
@shared_task
def archive_books():
    ten_years_ago = timezone.now() - timezone.timedelta(days=3650)
    books_to_archive = Book.objects.filter(published_date__lt=ten_years_ago, is_archived=False)
    for book in books_to_archive:
        book.is_archived = True
        book.save()
    return f"Archived {books_to_archive.count()} books."


