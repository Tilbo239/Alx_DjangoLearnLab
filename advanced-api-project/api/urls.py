from django.urls import path
from .views import BookCreateView, BookUpdateView, BookDeleteView, BookDetailView, BookListView, AuthorCreateView, AuthorListView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
  path('books/', BookListView.as_view(), name="book-list"),
  path('books/create', BookCreateView.as_view(), name="book-create"),
  path('books/<int:pk>/detail', BookDetailView.as_view(), name="book-detail"),
  path('books/update', BookUpdateView.as_view(), name="book-update"),
  path('books/delete', BookDeleteView.as_view(), name="book-delete"),
   path('authors/', AuthorListView.as_view(), name="author-list"),
  path('author/create', AuthorCreateView.as_view(), name="author-create"),
  path('login/', obtain_auth_token, name='login')
  
]