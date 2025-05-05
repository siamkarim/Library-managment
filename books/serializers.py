
from rest_framework import serializers
from .models import Book, Author
from user.models import User
from django.contrib.auth import get_user_model



class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Book
        #named fields to avoid exposing sensitive data
        fields = ('id', 'title', 'author', 'published_date', 'isbn', 'genre', 'description', 'is_archived')

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        #named fields to avoid exposing sensitive data
        fields = ('id', 'name', 'biography', 'date_of_birth')
        

def validate_author(self, value):
    if not User.objects.filter(id=value.id).exists():
        raise serializers.ValidationError("Author does not exist.")
    return value
       