from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


#  Registration
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            return redirect('login')

    else:
        form = CustomUserCreationForm()
    return render(request, "blog/register.html", {"form": form} )

# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect("profile")
        else:
            messages.error(request, "Invalid username or password!")

    form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})


# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def profile_view(request):
    if request.method == "POST":
        request.user.email = request.POST.get("email", "")
        request.user.save()
        return redirect("profile")
    return render(request, "blog/profile.html", {"user": request.user})

