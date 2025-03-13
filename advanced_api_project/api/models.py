from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_date = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)