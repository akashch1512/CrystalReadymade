from django.shortcuts import render
from django.http import HttpResponse
from .models import EightElementSection, Product
# Create your views here.
def index(request):
    New_Arrivals = EightElementSection.objects.get(name="New Arrivals")
    product_names = [
        New_Arrivals.product1,
        New_Arrivals.product2,
        New_Arrivals.product3,
        New_Arrivals.product4,
        New_Arrivals.product5,
        New_Arrivals.product6,
        New_Arrivals.product7,
        New_Arrivals.product8,
    ]
    
    # Retrieve all products in one query
    products = Product.objects.filter(product_name__in=product_names)
    print(products)
    # Pass the New_Arrivals object and the products to the template
    return render(request, 'shop/index.html', {'show_popup': False, 'New_Arrivals': New_Arrivals, 'products': products})

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
