from django.shortcuts import render, redirect
from core.users_api_service import register_user, login_user, logout_user
from django.contrib import messages

def logout_view(request):
    data = {}
    data['token'] = request.session['token']
    logout_user(data)
    request.session['token'] = None
    return redirect('/')

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
            request.session['token'] = response.get('token')
            return redirect('home')
        else:
            messages.error(request, 'Registration failed. Please try again.')
    else:
        return render(request, 'accounts/register.html')

def login_view(request):
    if request.method == 'POST':
        data = {
            'email': request.POST.get('email'),
            'password': request.POST.get('password'),
            # Add more fields as needed
        }
        response = login_user(data)
        if response['status'] == 'success':
            request.session['email'] = data['email']
            request.session['token'] = response.get('token')
            return redirect('apps.accounts:home')
        else:
            messages.error(request, 'Login failed. Please try again.')
    else:
        return render(request, 'sod/login.html')

def home_view(request):
    if request.method == 'POST':
        pass
    else:
        if request.session['token'] is None:
            return redirect('login')
        else:
            token = request.session['token']
            return render(request, 'accounts/home.html')