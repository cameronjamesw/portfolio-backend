from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("bio", "phone_number", "profile_image")}),
    )
