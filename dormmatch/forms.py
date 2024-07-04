# forms.py
from django import forms
from .models import TenantProfile

class SignUpForm(forms.ModelForm):
    class Meta:
        model = TenantProfile
        fields = ['user_id', 'last_name', 'first_name', 'age', 'contact_number', 'email', 'school', 'degree_program']
