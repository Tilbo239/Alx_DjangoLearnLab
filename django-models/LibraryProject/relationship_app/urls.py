from django.urls import path
from . import views
from .views import list_books
from .views import register_view, login_view, logout_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', list_books, name='book_list'),  # For the function-based view
    path('', views.LibraryDetailView.as_view(), name='library_detail'),  # For the class-based view
    path('', register_view, name='register'),
    path('', login_view, name='login'),
    path('', logout_view, name='logout'),
]