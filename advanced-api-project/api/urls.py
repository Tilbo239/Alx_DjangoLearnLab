from django.urls import path
from .views import CreateView, UpdateView, DeleteView, DetailView, ListView, AuthorCreateView, AuthorListView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
  path('books/', ListView.as_view(), name="book-list"),
  path('books/create', CreateView.as_view(), name="book-create"),
  path('books/<int:pk>/detail', DetailView.as_view(), name="book-detail"),
  path('books/update', UpdateView.as_view(), name="book-update"),
  path('books/delete', DeleteView.as_view(), name="book-delete"),
   path('authors/', AuthorListView.as_view(), name="author-list"),
  path('author/create', AuthorCreateView.as_view(), name="author-create"),
  path('login/', obtain_auth_token, name='login')
  
]