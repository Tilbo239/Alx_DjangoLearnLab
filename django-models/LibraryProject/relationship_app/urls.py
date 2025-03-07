from django.urls import path
from . import views
from .views import list_books
from  . import views 


app_name = 'relationship_app'

urlpatterns = [
    path('books/', list_books, name='book_list'), 
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # For the class-based view
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),

    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/', views.edit_book, name='edit_book'),
    path('delete_book/', views.delete_book, name='delete_book'),
    
]