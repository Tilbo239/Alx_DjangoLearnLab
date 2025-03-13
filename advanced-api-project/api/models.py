from django.db import models

class Author(models.Model):

    """
    Model representing an author.
    An author can have multiple books.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Model representing a book.
    Each book is linked to an author via a ForeignKey relationship.
    """
    title = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"