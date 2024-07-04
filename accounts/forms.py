 # accounts/forms.py
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = (
              "email",
            "username",
            "last_name",
            "first_name",
            "contact_number",
            "email",
            "school",
            "degree_program",
            "age",
        )

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
             "email",
            "username",
            "last_name",
            "first_name",
            "contact_number",
            "email",
            "school",
            "degree_program",
            "age",
        )

        