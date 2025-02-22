from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),  # For the function-based view
    path('', views.LibraryDetailView.as_view(), name='library_detail'),  # For the class-based view
]