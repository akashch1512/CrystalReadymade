from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from shop.models import Profile

def user_info(request):
    if request.user.is_authenticated:
        profile = getattr(request.user, 'profile', None)

        if request.method == 'POST':
            # Handling profile photo upload
            if 'profile_photo' in request.FILES:
                profile_photo = request.FILES['profile_photo']
                profile.user_profile_photo = profile_photo
                profile.save()

            # Handling other fields and updating them
            if 'firstname' in request.POST:
                request.user.first_name = request.POST['firstname']
            if 'lastname' in request.POST:
                request.user.last_name = request.POST['lastname']
            if 'email' in request.POST:
                request.user.email = request.POST['email']
            if 'username' in request.POST:
                request.user.username = request.POST['username']
            
            if profile:
                if 'mobile' in request.POST:
                    request.user.profile.mobile = request.POST['mobile']
                if 'address_line_one' in request.POST:
                    profile.address_line_one = request.POST['address_line_one']
                if 'address_line_two' in request.POST:
                    profile.address_line_two = request.POST['address_line_two']
                if 'address_line_three' in request.POST:
                    profile.address_line_three = request.POST['address_line_three']
                if 'city' in request.POST:
                    profile.city = request.POST['city']
                if 'state' in request.POST:
                    profile.state = request.POST['state']
                if 'zip' in request.POST:
                    profile.zip = request.POST['zip']

                # Save the updated profile information
                profile.save()

            # Save the user information
            request.user.save()

            # Redirect after updating
            return redirect('login_view')  # Adjust this to the correct URL name for the profile page

        # Determine if fields are valid or not and assign 'is-valid' or 'is-invalid'
        email_valid = bool(request.user.email)
        username_valid = bool(request.user.username)
        firstname_valid = bool(request.user.first_name)
        lastname_valid = bool(request.user.last_name)
        last_login_valid = bool(request.user.last_login)
        user_profile_photo_valid = bool(profile and profile.user_profile_photo)
        mobile_valid = bool(profile and profile.mobile)
        address_line_one_valid = bool(profile and profile.address_line_one)
        address_line_two_valid = bool(profile and profile.address_line_two)
        address_line_three_valid = bool(profile and profile.address_line_three)
        city_valid = bool(profile and profile.city)
        state_valid = bool(profile and profile.state)
        zip_valid = bool(profile and profile.zip)
        
        context = {
            'email': request.user.email,
            'email_valid': 'is-valid' if email_valid else 'is-invalid',
            'username': request.user.username,
            'username_valid': 'is-valid' if username_valid else 'is-invalid',
            'firstname': request.user.first_name,
            'firstname_valid': 'is-valid' if firstname_valid else 'is-invalid',
            'lastname': request.user.last_name,
            'lastname_valid': 'is-valid' if lastname_valid else 'is-invalid',
            'last_login': request.user.last_login,
            'last_login_valid': 'is-valid' if last_login_valid else 'is-invalid',
            'user_profile_photo': profile.user_profile_photo.url if user_profile_photo_valid else None,
            'user_profile_photo_valid': user_profile_photo_valid,
            'mobile': profile.mobile if profile else None,
            'mobile_valid': 'is-valid' if mobile_valid else 'is-invalid',
            'address_line_one': profile.address_line_one if profile else None,
            'address_line_one_valid': 'is-valid' if address_line_one_valid else 'is-invalid',
            'address_line_two': profile.address_line_two if profile else None,
            'address_line_two_valid': 'is-valid' if address_line_two_valid else 'is-invalid',
            'address_line_three': profile.address_line_three if profile else None,
            'address_line_three_valid': 'is-valid' if address_line_three_valid else 'is-invalid',
            'city': profile.city if profile else None,
            'city_valid': 'is-valid' if city_valid else 'is-invalid',
            'state': profile.state if profile else None,
            'state_valid': 'is-valid' if state_valid else 'is-invalid',
            'zip': profile.zip if profile else None,
            'zip_valid': 'is-valid' if zip_valid else 'is-invalid',
        }
        
        return render(request, 'members/userinfo.html', context)
    
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
