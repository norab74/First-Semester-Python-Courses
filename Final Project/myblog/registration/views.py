from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
from .models import *

def home(request):
    return render(request, 'home.html')

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if a user with the provided username exists
        if not User.objects.filter(username=username).exists():
            # Display an error message if the username does not exist
            messages.error(request, 'Invalid Username')
            return redirect('/login/')
        
        user = authenticate(username=username, password=password)
        
        if user is None:
            # Display an error message if authentication fails (invalid password)
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/blog/') #may change later
    
    return render(request, 'registration/login.html')

# Define a view function for the registration page
def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        # support templates that name password fields either password/password or password1/password2
        password1 = request.POST.get('password1') or request.POST.get('password')
        password2 = request.POST.get('password2') or password1

        errors = []

        if not username:
            errors.append("Username is required.")
        if not password1:
            errors.append("Password is required.")
        if password1 and password2 and password1 != password2:
            errors.append("Passwords do not match.")
        # optional password strength/length check (adjust as needed)
        if password1 and len(password1) < 8:
            errors.append("Password must be at least 8 characters long.")

        if User.objects.filter(username=username).exists():
            errors.append("Username already taken.")
        if email and User.objects.filter(email=email).exists():
            errors.append("An account with that email already exists.")

        if errors:
            for e in errors:
                messages.error(request, e)
            # re-render the form and preserve entered (non-sensitive) values
            context = {
                'first_name': first_name,
                'last_name': last_name,
                'username': username,
                'email': email,
            }
            return render(request, 'registration/register.html', context)

        # create and save the user
        user = User.objects.create_user(
            username=username,
            email=email or None,
            password=password1,
            first_name=first_name or '',
            last_name=last_name or ''
        )

        messages.success(request, "Account created successfully. Please log in.")
        return redirect('/login/')

    # GET
    return render(request, 'registration/register.html')


@require_http_methods(["GET", "POST"])
def logout_page(request):
    """
    Show a confirmation page on GET, and log out on POST.
    """
    logout(request)

    # GET: render the confirmation page
    return render(request, 'registration/logged_out.html')
