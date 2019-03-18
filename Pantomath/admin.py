from django.contrib import admin
from .models import Organization, InventoryItem, Sanction

# Register your models here.

admin.site.register(Organization)
admin.site.register(InventoryItem)
admin.site.register(Sanction)
