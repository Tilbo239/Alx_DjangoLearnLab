from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.shortcuts import get_object_or_404



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
            return redirect("posts")
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


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/new_post.html'
    
    def get_form_kwargs(self):
        """Pass the logged in user to the form."""
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
    def get_success_url(self):
        return reverse_lazy('posts')
    
    
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/new_post.html'

    def get_form_kwargs(self):
        """Pass the logged in user to the form."""
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
    def test_func(self):
        """Checks that the user is the author of the post."""
        post = self.get_object()  # Retrieves the post currently being edited
        return self.request.user == post.author  # Only the author can modify
    
    def get_success_url(self):
        return reverse_lazy('posts')


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('posts')  # Redirect after deletion

    def test_func(self):
        """Only the author of the post can delete it."""
        post = self.get_object()
        return self.request.user == post.author
    
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/new_comment.html"

    def form_valid(self, form):
        form.instance.author = self.request.user  # Associe l'utilisateur actuel
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['post_id'])  # Associe le post
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('post-detail',  kwargs={'pk': self.object.post.pk})
    
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/new_comment.html"


    def test_func(self):
        """Vérifie que l'utilisateur est bien l'auteur du commentaire"""
        comment = self.get_object()
        return self.request.user == comment.author
    
    def get_success_url(self):
        return reverse_lazy('post-detail',  kwargs={'pk': self.object.post.pk})
    
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = "blog/comment_confirm_delete.html"

    def test_func(self):
        """Vérifie que l'utilisateur est bien l'auteur du commentaire"""
        comment = self.get_object()
        return self.request.user == comment.author
    
    def get_success_url(self):
        return reverse_lazy('post-detail',  kwargs={'pk': self.object.post.pk})

