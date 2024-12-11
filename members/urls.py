from django.contrib import admin
from . import views
from django.urls import path
from django.contrib.auth.views import LogoutView

urlpatterns = [
     path('login/', views.login_view, name='login_view'),
     path('signup/', views.signup_view, name='signup_view'),
      path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
      path('addproduct/',views.addproduct, name='addproduct'),
      path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
      path('product/',views.view_products, name='view_products'),
]
