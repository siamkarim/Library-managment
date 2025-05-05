from rest_framework import generics, status
from rest_framework.response import Response
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.utils.translation import gettext_lazy as _


class BookListView(generics.ListCreateAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request, *args, **kwargs):
        books = self.get_queryset()
        # except archive books
        books= books.exclude(is_archived=True)
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request, *args, **kwargs):
        book = self.get_object()
        serializer = self.get_serializer(book)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        book = self.get_object()
        serializer = self.get_serializer(book, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        book = self.get_object()
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class AuthorListView(generics.ListCreateAPIView):

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request, *args, **kwargs):
        authors = self.get_queryset()
        serializer = self.get_serializer(authors, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request, *args, **kwargs):
        author = self.get_object()
        serializer = self.get_serializer(author)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        author = self.get_object()
        serializer = self.get_serializer(author, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        author = self.get_object()
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




