# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class DormMatchAdminSite(admin.AdminSite):
    site_header = "DormMatch Administration"
    site_title = "DormMatch Admin Portal"
    index_title = "Welcome to DormMatch Admin"
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
    "email",
    "username",
    "last_name",
    "first_name",
    "contact_number",
    "email",
    "school",
    "degree_program",
    "age",
    "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + ((None,{"fields":("age",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None,{"fields":("age",)}),)
admin.site.register(CustomUser, CustomUserAdmin)