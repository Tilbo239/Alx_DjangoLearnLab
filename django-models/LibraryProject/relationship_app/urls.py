from django.urls import path
from . import views
from .views import list_books

urlpatterns = [
    path('', list_books, name='book_list'),  # For the function-based view
    path('', views.LibraryDetailView.as_view(), name='library_detail'),  # For the class-based view
]