from django.shortcuts import render
# from django.http import HttpResponse
# from .models import EightElementSection, Product

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def index(request):
    # Handle Search Query
    if request.method == "POST":
        search_query = request.POST.get("search_query", "").strip()
        if search_query:
            # Mock product data
            products = [
                {'name': 'Akash is for sale', 'description': 'Shop products from small business brands sold in Amazon\'s store. Discover more about the small businesses partnering with Amazon and Amazon\'s commitment to empowering them.', 'price': 99.99, 'image_url': 'https://via.placeholder.com/150'},
                {'name': 'Akash is for sale', 'description': 'Shop products from small business brands sold in Amazon\'s store. Discover more about the small businesses partnering with Amazon and Amazon\'s commitment to empowering them.', 'price': 49.99, 'image_url': 'https://via.placeholder.com/150'},
                {'name': 'Akash is for sale', 'description': 'Shop products from small business brands sold in Amazon\'s store. Discover more about the small businesses partnering with Amazon and Amazon\'s commitment to empowering them.', 'price': 29.99, 'image_url': 'https://via.placeholder.com/150'},
                {'name': 'Akash is for sale', 'description': 'Shop products from small business brands sold in Amazon\'s store. Discover more about the small businesses partnering with Amazon and Amazon\'s commitment to empowering them.', 'price': 19.99, 'image_url': 'https://via.placeholder.com/150'},
                {'name': 'Akash is for sale', 'description': 'Shop products from small business brands sold in Amazon\'s store. Discover more about the small businesses partnering with Amazon and Amazon\'s commitment to empowering them.', 'price': 9.99, 'image_url': 'https://via.placeholder.com/150'},
            ]
            # Render the search results page
            return render(request, 'shop/search.html', {'search_query': search_query, 'products': products})

        # Handle Login
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('ShopHome')  # Replace 'ShopHome' with your homepage URL name
            else:
                messages.error(request, 'Invalid username or password. Please try again.')

    # Show popup only if the user is not authenticated
    show_popup = not request.user.is_authenticated
    return render(request, 'shop/index.html', {'show_popup': show_popup})


def aboutus(request):
    return render(request,'shop/aboutus.html')

def contactus(request):
    return render(request,'shop/contactus.html')

def search(request):
    return render(request,'shop/search.html')

def productview(request):
    return render(request,'shop/productview.html')

def checkout(request):
    return render(request,'shop/checkout.html')

def trackingstatus(request):
    return render(request,'shop/trackingstatus.html')
