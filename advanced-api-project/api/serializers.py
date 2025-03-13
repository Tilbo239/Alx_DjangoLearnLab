from datetime import datetime
from rest_framework import serializers

from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):

    """
    Serializer for the Book model.
    Includes validation to ensure the publication year is not in the future.
    """
    
    class Meta:
        model = Book
        fields = '__all__'

        def validate(self, data):
            if data['publication_year'] > datetime.now().year:
                raise serializers.ValidationError("publication_year can not be in the future")
            return data

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.
    Also serializes associated books using a nested serializer.
    """
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['id', 'name', 'books']