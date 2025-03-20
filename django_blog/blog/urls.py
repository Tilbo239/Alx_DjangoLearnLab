from django.urls import path
from . import views
from  .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CommentCreateView, CommentUpdateView, CommentDeleteView

# app_name = 'blog'

urlpatterns = [

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'), 
    path("profile/", views.profile_view, name="profile"),

    path('posts/', PostListView.as_view(), name='posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), 
    path('post/new/', PostCreateView.as_view(), name='new-post'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='edit-post'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='delete-post'),

    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]
