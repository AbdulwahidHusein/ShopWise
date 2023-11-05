from django.contrib import admin
from .models import CustomUser, Buyer, Seller
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Buyer)
admin.site.register(Seller)
