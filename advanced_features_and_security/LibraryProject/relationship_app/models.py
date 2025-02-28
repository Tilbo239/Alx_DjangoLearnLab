from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.conf import settings


class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

#Create Book model with custom Permissions   
class Book(models.Model):
  class Meta:
     permissions = [
        ("can_add_book", "Can add book"),
        ("can_change_book", "Can change book"),
        ("can_delete_book", "Can delete book")
      ]
  title = models.CharField(max_length=120)
  author = models.ForeignKey(Author, on_delete= models.CASCADE, related_name="books")

  def __str__(self):
    return f"{self.title} - {self.author}"


class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book, related_name='libraries')

    def __str__(self):
        return self.name
    
class Librarian(models.Model):
    name = models.CharField(max_length=200)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarians')

    def __str__(self):
        return self.name
    

class UserProfile(models.Model):
  ROLE_CHOICES =[
    ('Admin', 'Admin'),
    ('Member', 'Member'),
    ('Librarian', 'Librarian'), 
  ]

  user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  role = models.CharField(max_length=15, choices=ROLE_CHOICES)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()