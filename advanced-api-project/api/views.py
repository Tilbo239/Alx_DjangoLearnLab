from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from rest_framework import generics


class CreateView(generics.CreateAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer

class ListView(generics.ListAPIView):
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    


class DetailView(generics.RetrieveAPIView):
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    

class UpdateView(generics.UpdateAPIView):
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class DeleteView(generics.DestroyAPIView):
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer