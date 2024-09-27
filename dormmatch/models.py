from django.db import models
from django.urls import reverse

class TenantProfile(models.Model):
    user_id = models.CharField(max_length=255, primary_key=True)
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    contact_number = models.CharField(max_length=15)  # Changed to CharField to handle different formats
    email = models.EmailField(unique=True)
    school = models.CharField(max_length=255)
    degree_program = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class DormInfo(models.Model):
    DORM_CLASS_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        
    ]
    DORM_TYPE_CHOICES = [
        ('solo', 'Solo'),
        ('shared', 'Shared'),
    ]
    OCCUPIED_STATUS_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    dorm_id = models.CharField(max_length=255, primary_key=True)
    dorm_class = models.CharField(max_length=1, choices=DORM_CLASS_CHOICES)
    dorm_type = models.CharField(max_length=6, choices=DORM_TYPE_CHOICES)
    capacity = models.PositiveIntegerField(default=0)
    occupied_status = models.CharField(max_length=3, choices=OCCUPIED_STATUS_CHOICES)
    dorm_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    description = models.TextField()

    def save(self, *args, **kwargs):
        if self.dorm_class == 'A' and self.dorm_type == 'solo':
            self.dorm_price = 16000
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.dorm_class} {self.dorm_type}'

class TransactionLog(models.Model):
    TRANSACTION_STATUS_CHOICES = [
        ('Paid', 'Paid'),
        ('Pending', 'Pending')
    ]
    transaction_id = models.CharField(max_length=255, primary_key=True)
    ref_number = models.CharField(max_length=255)
    booking = models.ForeignKey('Bookings', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=TRANSACTION_STATUS_CHOICES)

    def __str__(self):
        return f'Transaction {self.transaction_id} - {self.status}'

class Bookings(models.Model):
    BOOK_STATUS_CHOICES = [
        ('For Waitlisted', 'For Waitlisted'),
        ('For Payment', 'For Payment'),
        ('For Occupying', 'For Occupying'),
        ('Cancelled', 'Cancelled'),
    ]
    booking_id = models.CharField(max_length=255, primary_key=True)
    user = models.ForeignKey(TenantProfile, on_delete=models.CASCADE)
    dorm = models.ForeignKey(DormInfo, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    book_status = models.CharField(max_length=20, choices=BOOK_STATUS_CHOICES)

    def __str__(self):
        return f'Booking {self.booking_id} - {self.book_status}'


