from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

def user_info(request):
    if request.user.is_authenticated:
        profile = getattr(request.user, 'profile', None)
        if profile:
            context = {
                'email': request.user.email,
                'username': request.user.username,
                'firstname': request.user.first_name,
                'lastname': request.user.last_name,
                'last_login': request.user.last_login,
                'user_profile_photo': profile.user_profile_photo.url if profile.user_profile_photo else None,
                'mobile': profile.mobile,
                'address_line_one': profile.address_line_one,
                'address_line_two': profile.address_line_two,
                'address_line_three': profile.address_line_three,
                'city': profile.city,
                'state': profile.state,
                'zip': profile.zip,
            }
        else:
            context = {
                'email': request.user.email,
                'username': request.user.username,
                'firstname': request.user.first_name,
                'lastname': request.user.last_name,
                'last_login': request.user.last_login,
                'user_profile_photo': None,  # Or a default placeholder URL
                'mobile': None,
                'address_line_one': None,
                'address_line_two': None,
                'address_line_three': None,
                'city': None,
                'state': None,
                'zip': None,
            }
        return render(request, 'members/userinfo.html', {context})

    else:
        return redirect('login')  # Redirects unauthenticated users to the login page

def login_view(request):
    if request.user.is_authenticated:
        return user_info(request)
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
            return redirect('ShopHome')  # Replace 'home' with your homepage URL name
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
