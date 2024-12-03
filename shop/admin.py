from django.contrib import admin

# Register your models here.
from .models import Product, User_auth, EightElementSection,Profile

admin.site.register(Product)

admin.site.register(User_auth)

admin.site.register(EightElementSection)

admin.site.register(Profile)