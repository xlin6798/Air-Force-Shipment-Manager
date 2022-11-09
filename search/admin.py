from django.contrib import admin

from .models import Product, SpCode, HazClass

admin.site.register(Product)
admin.site.register(SpCode)
admin.site.register(HazClass)