from .models import PurchaseOrderHeader, PurchaseOrderLine
from django.contrib import admin

admin.site.register(PurchaseOrderHeader)
admin.site.register(PurchaseOrderLine)