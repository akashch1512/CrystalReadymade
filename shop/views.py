from django.shortcuts import render
# from django.http import HttpResponse
# from .models import EightElementSection, Product

# Create your views here.
def index(request):
    if request.method == 'POST':
        query = request.POST.get("search_query")  # Corrected the typo
        products = [
        {'name': 'akash is for sell', 'description': 'Shop products from small business brands sold in Amazon"s store. Discover more about the small businesses partnering with Amazon and Amazon"s commitment to empowering them.', 'price': 99.99, 'image_url': 'https://via.placeholder.com/150'},
        {'name': 'akash is for sell', 'description': 'Shop products from small business brands sold in Amazon"s store. Discover more about the small businesses partnering with Amazon and Amazon"s commitment to empowering them.', 'price': 49.99, 'image_url': 'https://via.placeholder.com/150'},
        {'name': 'akash is for sell', 'description': 'Shop products from small business brands sold in Amazon"s store. Discover more about the small businesses partnering with Amazon and Amazon"s commitment to empowering them.', 'price': 29.99, 'image_url': 'https://via.placeholder.com/150'},
        {'name': 'akash is for sell', 'description': 'Shop products from small business brands sold in Amazon"s store. Discover more about the small businesses partnering with Amazon and Amazon"s commitment to empowering them.', 'price': 19.99, 'image_url': 'https://via.placeholder.com/150'},
        {'name': 'akash is for sell', 'description': 'Shop products from small business brands sold in Amazon"s store. Discover more about the small businesses partnering with Amazon and Amazon"s commitment to empowering them.', 'price': 9.99, 'image_url': 'https://via.placeholder.com/150'},
    ]
        return render(request, 'shop/search.html', {'search_query': query, 'products': products})
    show_popup = not(request.user.is_authenticated)
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
