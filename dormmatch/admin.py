from django.contrib import admin
from .models import *

admin.site.register(TenantProfile)
admin.site.register(DormInfo)
admin.site.register(Bookings)
admin.site.register(TransactionLog)
