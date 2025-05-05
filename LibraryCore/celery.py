from celery import Celery
from celery.schedules import crontab
from django.conf import settings


app = Celery('LibraryCore')
app.config_from_object('django.conf:settings', namespace='CELERY')
#run after every 30 minutes and checked books which is published in 10 years and archived them
app.conf.beat_schedule = {
    'archive_books': {
        'task': 'books.tasks.archive_books',
        'schedule': crontab(minute='*/30'),  # every 30 minutes
    },
}
app.autodiscover_tasks()
