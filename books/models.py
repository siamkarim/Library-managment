from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='books')
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    pages = models.IntegerField()
    cover_image = models.URLField(blank=True, null=True)
    language = models.CharField(max_length=30)
    genre = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    is_archived = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=255)
    biography = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    

    def __str__(self):
        return self.name
    

