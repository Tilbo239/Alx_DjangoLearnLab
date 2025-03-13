from rest_framework import generics 
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


"""
This module defines views for the Book model using Django REST framework.
Classes:
    BookViewSet: A viewset that provides CRUD operations for Book instances.
Authentication and Permissions:
    - BookViewSet: This viewset enforces authentication and permissions:
        - IsAuthenticated: Ensures that the user is authenticated.
        - IsAdminUser: Ensures that the user is an admin.
    Users must be both authenticated and have admin privileges to perform any operations (create, read, update, delete) on the Book instances through this viewset.
"""
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


    

