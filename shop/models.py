from django.db import models
from django.contrib.auth.models import User
from django.db import models

class Product(models.Model):
    # Basic Details
    name = models.CharField(max_length=100, verbose_name="Product Name")
    
    # Image Handling - For multiple images
    main_image = models.CharField(max_length=255, blank=True, null=True, verbose_name="Main Image")
    additional_images = models.JSONField(blank=True, null=True, help_text="Store additional image URLs as a JSON array")

    # Pricing Details
    original_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Original Price")
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Discounted Price")
    
    # Inventory and Stock
    stock_quantity = models.PositiveIntegerField(default=0, verbose_name="Stock Quantity")
    is_available = models.BooleanField(default=True, verbose_name="Is Available")

    # Description and Features
    short_description = models.CharField(blank=True, verbose_name="Short Description")
    detailed_description = models.TextField(blank=True, verbose_name="Detailed Description")

    # Product Categories and Tags
    category = models.CharField(max_length=50, verbose_name="Category")
    tags = models.CharField(blank=True, help_text="Comma-separated tags for the product")

    # Timestamps
    published_date = models.DateField(auto_now_add=True, verbose_name="Published Date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Last Updated")

    # Metadata
    sku = models.CharField(max_length=100, unique=True, verbose_name="SKU")
    brand = models.CharField(max_length=100, blank=True, verbose_name="Brand")
    weight = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Weight (kg)")
    dimensions = models.CharField(max_length=50, blank=True, help_text="Product dimensions (e.g., LxWxH)")

    # SEO Fields
    meta_title = models.CharField(max_length=100, blank=True, help_text="Meta title for SEO")
    meta_description = models.TextField(blank=True, help_text="Meta description for SEO")

    @classmethod
    def get_all(cls):
        """Fetch all products."""
        return cls._products

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    

# Separate model for managing multiple images per product
class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name="images", on_delete=models.CASCADE)
    image = models.CharField(max_length=255, blank=True, null=True, verbose_name="Product Image")
    alt_text = models.CharField(max_length=255, blank=True, verbose_name="Alt Text")
    
    def __str__(self):
        return f"Image for {self.product.name}"

    class Meta:
        verbose_name = "Product Image"
        verbose_name_plural = "Product Images"

class User_auth(models.Model):
    Email = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.Email
    
class SectionElement(models.Model):
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
    product9 = models.ForeignKey(Product, on_delete=models.SET_NULL, related_name="section_product9", null=True, blank=True)
    product10 = models.ForeignKey(Product, on_delete=models.SET_NULL, related_name="section_product10", null=True, blank=True)
    product11 = models.ForeignKey(Product, on_delete=models.SET_NULL, related_name="section_product11", null=True, blank=True)
    product12 = models.ForeignKey(Product, on_delete=models.SET_NULL, related_name="section_product12", null=True, blank=True)

    def __str__(self):
        return self.name
    
    @classmethod
    def get_by_name(cls, section_name):
        return cls.objects.filter(name=section_name).first()

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