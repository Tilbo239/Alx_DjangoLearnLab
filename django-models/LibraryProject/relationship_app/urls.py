from django.urls import path
from . import views
from .views import list_books
from  . import views 
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', list_books, name='book_list'),  # For the function-based view
    path('', views.LibraryDetailView.as_view(), name='library_detail'),  # For the class-based view
    path('', views.register_view, name='register'),
    path('', LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('', LogoutView.as_view(template_name='auth/logout.html'), name='logout'),
]