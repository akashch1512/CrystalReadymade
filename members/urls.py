from django.contrib import admin
from . import views
from django.urls import path
urlpatterns = [
     path('login/', views.login_view, name='login_view'),
     path('signup/', views.signup_view, name='signup_view'),
]
