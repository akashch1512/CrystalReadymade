from django.contrib import admin

# Register your models here.
from .models import Product, User_auth, EightElementSection

admin.site.register(Product)

admin.site.register(User_auth)

admin.site.register(EightElementSection)