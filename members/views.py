from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from shop.models import Profile


import requests
import base64

IMGUR_CLIENT_ID = '9d14773d02e6ac0'


import base64
import requests

IMGUR_CLIENT_ID = '9d14773d02e6ac0'


def upload_to_imgur(image_file):
    """Uploads image to Imgur and returns the URL."""
    url = "https://api.imgur.com/3/image"
    headers = {"Authorization": f"Client-ID {IMGUR_CLIENT_ID}"}
    
    # Read image bytes and encode to base64
    encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
    data = {"image": encoded_image}
    
    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        print("Upload successful")
        return response.json()["data"]["link"]  # Return the URL
    else:
        print("Imgur upload failed with status code:", response.status_code)
        return None

def user_info(request):
    if request.user.is_authenticated:
        profile = getattr(request.user, 'profile', None)

        if request.method == 'POST':
            # Handle profile photo upload and save to Imgur
            if 'profile_photo' in request.FILES:
                img_url = upload_to_imgur(request.FILES['profile_photo'])
                if img_url:
                    print(img_url)
                    profile.user_profile_photo = img_url  # Save the Imgur URL to database
                    profile.save()
                else:
                    # Handle Imgur upload failure
                    messages.error(request, "Failed to upload image to Imgur.")

            # Handling other user fields
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
                    profile.mobile = request.POST['mobile']
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

                profile.save()

            # Save the user information
            request.user.save()

            # Redirect after saving
            return redirect('login_view')

        context = {
            'email': request.user.email,
            'username': request.user.username,
            'firstname': request.user.first_name,
            'lastname': request.user.last_name,
            'mobile': profile.mobile,
            'address_line_one': profile.address_line_one,
            'address_line_two': profile.address_line_two,
            'address_line_three': profile.address_line_three,
            'city': profile.city,
            'state': profile.state,
            'zip': profile.zip,
            'user_profile_photo': profile.user_profile_photo  # Send the Imgur image URL to the template
        }

        return render(request, 'members/userinfo.html', context)

    else:
        return redirect('login')

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
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')  # Replace 'login' with your login page URL name
        except Exception as e:
            messages.error(request, f'Error creating account: {e}')

    # Render the signup page template
    return render(request, 'members/signup.html')  # Replace 'app_name' with your app's name
