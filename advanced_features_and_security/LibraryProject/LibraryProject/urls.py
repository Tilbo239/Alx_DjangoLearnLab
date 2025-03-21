"""
URL configuration for LibraryProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
# from relationship_app import views  # replace 'my_app' with the actual app name

urlpatterns = [
    path('admin/', admin.site.urls),
    path('relationship_app/', include('relationship_app.urls')),  # include the app's URLs
    # path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    # path('register/', views.register_view, name='register'),
    # path('login/', views.login_view, name='login'),
    # path('logout/', views.logout_view, name='logout'),
]

# Add this line to serve media files in development (only)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


