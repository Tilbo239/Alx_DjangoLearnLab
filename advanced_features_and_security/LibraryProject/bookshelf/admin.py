from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filters = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author', 'publication_year')


admin.site.register(Book)

class CustomUserAdmin(UserAdmin):
    # Add the fields to the fieldsets
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Information', {'fields': ('date_of_birth', 'profile_photo')}),
    )
    
    # If you want these fields to appear in the "add user" form
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Information', {
            'classes': ('wide',),
            'fields': ('date_of_birth', 'profile_photo'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
