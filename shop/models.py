from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    product_name = models.CharField(max_length=50)  # Name of the product
    image = models.ImageField(upload_to="shop/images", default="", null=True, blank=True)
    original_price = models.DecimalField(max_digits=10, decimal_places=2, default="")  # Product price
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, default="")  # Product price
    description = models.TextField()  # Detailed description
    published_date = models.DateField()  # Date when the product was published
    category = models.CharField(max_length=50,default="")
    category = models.CharField(max_length=50,default="")


    def __str__(self):
        return self.product_name
    
class User_auth(models.Model):
    Email = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.Email
    
class EightElementSection(models.Model):
    name = models.CharField(max_length=100, verbose_name="Section Name")
    
    # Fields for linking up to 8 products
    product1 = models.ForeignKey(Product, on_delete=models.SET_NULL, related_name="section_product1", null=True, blank=True)
    product2 = models.ForeignKey(Product, on_delete=models.SET_NULL, related_name="section_product2", null=True, blank=True)
    product3 = models.ForeignKey(Product, on_delete=models.SET_NULL, related_name="section_product3", null=True, blank=True)
    product4 = models.ForeignKey(Product, on_delete=models.SET_NULL, related_name="section_product4", null=True, blank=True)
    product5 = models.ForeignKey(Product, on_delete=models.SET_NULL, related_name="section_product5", null=True, blank=True)
    product6 = models.ForeignKey(Product, on_delete=models.SET_NULL, related_name="section_product6", null=True, blank=True)
    product7 = models.ForeignKey(Product, on_delete=models.SET_NULL, related_name="section_product7", null=True, blank=True)
    product8 = models.ForeignKey(Product, on_delete=models.SET_NULL, related_name="section_product8", null=True, blank=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_profile_photo = models.CharField(blank=True, null=True)
    mobile = models.CharField(max_length=16, blank=True, null=True)
    address_line_one = models.CharField(max_length=255, blank=True, null=True)
    address_line_two = models.CharField(max_length=255, blank=True, null=True)
    address_line_three = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    zip = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.user.username