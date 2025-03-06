from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.

class Book(models.Model):
  title = models.CharField(max_length=200)
  author = models.CharField(max_length=100)
  publication_year = models.IntegerField()

  def __str__(self):
    return f"title : {self.title}, author : {self.author}, publication year : {self.publication_year}"
  

class CustomUser(AbstractUser):
  date_of_birth = models.DateField(null=True, blank=True)
  profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

  def __str__(self):
    return self.username
  
class CustomUserManager(BaseUserManager):
   
   def create_user(self, username, email, password=None, **extra_fields):
      
      email = self.normalize_email(email)
      user = self.model(username=username, email=email, **extra_fields)
      user.set_password(password)
      user.save(using=self._db)

      return user
   

   def create_superuser(self, username, email, password=None, **extra_fields):
      
      extra_fields.setdefault('is_staff', True)
      extra_fields.setdefault('is_superuser', True)

      return self.create_user(username, email, password, **extra_fields)
   

class Comment(models.Model):
  user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
  book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
  comment = models.TextField(blank=True)
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    permissions = [
      ("can_view", "Can view the posts"),
      ("can_create", "Can create post"),
      ("can_edit", "Can edit the posts"),
      ("can_delete", "Can delete the posts"),
    ]

  def __str__(self):
    return f"{self.user.username} commented on {self.book.title}"
   
