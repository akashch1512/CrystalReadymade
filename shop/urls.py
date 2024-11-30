from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='ShopHome'),
    path('ContactUs/', views.contactus, name='ContactUs'),
    path('AboutUs/', views.aboutus, name='AboutUs'),
    path('TrackingStatus/', views.trackingstatus, name='TrackingStatus'),
    path('Search/', views.search, name='Search'),
    path('ProductView/', views.productview, name='ProductView'),
    path('CheckOut/', views.checkout, name='CheckOut'),
    
]
