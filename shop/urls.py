from django.contrib import admin
from django.urls import path
from django.conf import settings  # Import settings
from django.conf.urls.static import static  # Import static for media handling
from . import views
# <!-- {% url 'ProductView' product.id %} -->
urlpatterns = [
    path('', views.index, name='ShopHome'), 
    path('ContactUs/', views.contactus, name='ContactUs'),
    path('AboutUs/', views.aboutus, name='AboutUs'),
    path('TrackingStatus/', views.trackingstatus, name='TrackingStatus'),
    path('Search/', views.search, name='Search'),
    path('product/<int:product_id>/', views.ProductView, name='ProductView'),
    path('CheckOut/', views.checkout, name='CheckOut'),
    path('LikedProducts/', views.likedproducts, name='LikedProducts'),
    path('Cart/', views.cart, name='cart'),
]

# Add media URL pattern during development
if settings.DEBUG:  # Serve media files only in development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
