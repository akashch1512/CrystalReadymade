from django.shortcuts import render
# from django.http import HttpResponse
# from .models import EightElementSection, Product

# Create your views here.
def index(request):
    
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
