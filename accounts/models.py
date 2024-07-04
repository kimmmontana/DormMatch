from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    username = models.CharField(max_length=255, primary_key=True)
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    age = models.PositiveIntegerField(null=True, blank=True)
    contact_number = models.CharField(max_length=15)  # Changed to CharField to handle different formats
    email = models.EmailField(unique=True)
    school = models.CharField(max_length=255)
    degree_program = models.CharField(max_length=255)
# Create your models here.
