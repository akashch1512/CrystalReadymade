from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
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
    if request.method == 'POST':
        # Collect data from the form
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Print the collected data for debugging
        print(first_name, last_name, username, email, password, confirm_password)

        # Validation
        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            print("match")
            return render(request, 'members/signup.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            print("username")
            return render(request, 'members/signup.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered.')
            print("email")
            return render(request, 'members/signup.html')

        # Create the user
        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            user.save()
            print("yeh")
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')  # Replace 'login' with your login page URL name
        except Exception as e:
            messages.error(request, f'Error creating account: {e}')
            print("error")

    # Render the signup page template
    return render(request, 'members/signup.html')  # Replace 'app_name' with your app's name
