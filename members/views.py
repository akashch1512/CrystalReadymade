from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        # Fetch username and password from the form
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Log the user in and redirect to homepage
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            return redirect('home')  # Replace 'home' with your homepage URL name
        else:
            # Show error message on invalid credentials
            messages.error(request, 'Invalid username or password. Please try again.')

    # Render the login page template
    return render(request, 'members/login.html')  # Replace 'app_name' with your app's name


def signup_view(request):
    return render(request, 'members/signup.html')  # Replace 'app_name' with your app's name
