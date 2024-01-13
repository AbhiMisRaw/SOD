from django.shortcuts import render

# Create your views here.
from core.users_api_service import register_user,login_user,logout_user
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    data={}
    #data['email'] = request.session['email'] 
    data['token'] = request.session['token']
    logout_user(data)
    request.session['token'] = None
    return redirect('login')



def register_view(request):
    if request.method == 'POST':
        data = {
            'email': request.POST['email'],
            'password': request.POST['password'],
            # Add more fields as needed
        }
        response = register_user(data)
        if response['status'] == 'success':  
            request.session['email'] = data['email']
            # If the API returns a token, you can store it in the session as well
            request.session['token'] = response.get('token')
            return redirect('home')
        else:
            # If the registration fails, you can show an error message
            messages.error(request, 'Registration failed. Please try again.')
    else:
        return render(request, 'accounts/register.html')



def login_view(request):
    if request.method == 'POST':
        data = {
            'email': request.POST['email'],
            'password': request.POST['password'],
            # Add more fields as needed
        }
        response = login_user(data)
        if response['status'] == 'success':  # Adjust this based on the actual API response
            # Store the user's information in the session
            request.session['email'] = data['email']
            # If the API returns a token, you can store it in the session as well
            request.session['token'] = response.get('token')
            return redirect('home')
        else:
            messages.error(request, 'Login failed. Please try again.')
    else:
        return render(request, 'accounts/login.html')

def home_view(request):
    if request.method == 'POST':
        pass
    else:
        if request.session['token'] is None:
            return redirect('login')
        else:
            token = request.session['token']
            return render(request, 'accounts/home.html')