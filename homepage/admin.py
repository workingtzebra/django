from django.contrib import admin
from .models import Contact, CustomUser  # Import the Contact and CustomUser models

# Admin for Contact
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')

admin.site.register(Contact, ContactAdmin)

# Admin for CustomUser
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date_of_birth', 'bio')  # Add other fields if you want
    # If you want to include fields from PermissionsMixin, you can add them here

admin.site.register(CustomUser, CustomUserAdmin)