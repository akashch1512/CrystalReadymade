from django.contrib import admin

# Register your models here.
from .models import Product, User_auth, SectionElement,Profile

admin.site.register(Product)

admin.site.register(User_auth)

admin.site.register(SectionElement)

admin.site.register(Profile)