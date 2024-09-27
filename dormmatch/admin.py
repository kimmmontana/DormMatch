from django.contrib import admin
from .models import *

class DormMatchAdminSite(admin.AdminSite):
    site_header = "DormMatch Administration"
    site_title = "DormMatch Admin Portal"
    index_title = "Welcome to DormMatch Admin"

admin_site = DormMatchAdminSite(name='dormmatch_admin')

admin.site.register(TenantProfile)
admin.site.register(DormInfo)
admin.site.register(Bookings)
admin.site.register(TransactionLog)


