from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Book
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from django.views.generic.detail import DetailView
from .models import Library

def list_books(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'relationship_app/list_books.html', context)



class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    def get_queryset(self):
        return Library.objects.all()
   
#register view
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login(request, user)
            return redirect('relationship_app:book_list')  # Remplace 'home' par ton URL d'accueil
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect("relationship_app:book_list")
        else:
            messages.error(request, "Invalid username or password!")

    form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})

# Logout view
def logout_view(request):
    logout(request)
    return redirect('relationship_app:login')

# Check user role Admin
def is_admin(user):
    return user.userprofile.role == 'Admin'

# Check user role Librarian
def is_librarian(user):
    return user.userprofile.role == 'Librarian'

# Check user role Member
def is_member(user):
    return user.userprofile.role == 'Member'


# Admin View
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian View
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

#member View
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    pass

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    pass

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    pass