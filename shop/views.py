from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import SectionElement, Product , Deal_of_the_day_section, Profile
from django.contrib.auth.decorators import login_required

def index(request):
    # Handle Search Query
    if request.method == "POST":
        search_query = request.POST.get("search_query", "").strip()
        if search_query:
            # Mock product data
            products = Product.objects.all()
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
    trending = SectionElement.get_by_name("Trending")
    top_rated = SectionElement.get_by_name("Top Rated")
    new_arrivals = SectionElement.get_by_name("New Arrivals")
    best_sellers = SectionElement.get_by_name("best sellers")
    new_products = SectionElement.get_by_name("New Products")
    deal_of_the_day_1 = Deal_of_the_day_section.get_by_name('Product1')
    deal_of_the_day_2 = Deal_of_the_day_section.get_by_name('Product2')
    
    
    context = {
    'show_popup': show_popup,
    'trending': trending,
    'new_arrivals' : new_arrivals,
    'top_rated' : top_rated,
    'new_products': new_products,
    'best_sellers' : best_sellers,
    'deal_of_the_day_1' : deal_of_the_day_1,
    'deal_of_the_day_2' : deal_of_the_day_2,
    }
    return render(request, 'shop/index.html', context)

def aboutus(request):
    return render(request,'shop/aboutus.html')

def contactus(request):
    return render(request,'shop/contactus.html')

def search(request):
    return render(request,'shop/search.html')

def ProductView(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'shop/productview.html', {'product': product})

def checkout(request):
    return render(request,'shop/checkout.html')

def trackingstatus(request):
    return render(request,'shop/trackingstatus.html')

def likedproducts(request):
    return render(request, 'shop/likedproducts.html')

def cart(request):
    return render(request, 'shop/cart.html')
