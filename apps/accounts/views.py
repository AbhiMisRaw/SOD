from django.shortcuts import render, redirect
from core.users_api_service import register_user, login_user, logout_user
from django.contrib import messages
from .forms import SignUpForm
from .actions.user_profile import do_create_user_profile, get_or_create_user_profile
from .actions import user as user_actions   


def logout_view(request):
    data = {}
    data['token'] = request.session['token']
    logout_user(data)
    request.session['token'] = None
    return redirect('/')

def register_view(request):
    msg = None
    success = False
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            # data = {
            # 'username': request.POST['email'],
            # 'password': request.POST['password1'],
            #      }
            user_exists = user_actions.is_user_created(request.POST['email'])
            user_profile_exists = user_actions.is_user_created(request.POST['email'])
            if user_exists is False:
                if user_profile_exists is False:
                    user_id = user_actions.get_or_create_user(request.POST['email'],request.POST['password1'])
                    if user_id is not None:
                        profile = get_or_create_user_profile(user_id=user_id)
                        if profile is not None:
                            # request.session['email'] = data['username']
                            # request.session['user_id'] = user_id  
                            msg = 'User registration successful. Please click Sign In.'
                            success = True
                        else:
                            msg = "There was a problem in registration. Please contact support team to fix the issue."
                            success = False
            else:
                if user_profile_exists is True:
                    msg = 'A user already exists with provided email. Please choose another email.'
                    success = False
        else:
            msg = 'There was problem with provided input. Please fix the errors and try again.'
            success = False
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})

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
            return redirect('index')
        else:
            messages.error(request, 'Login failed. Please try again.')
    else:
        return render(request, 'accounts/login.html')

def home_view(request):
    if request.method == 'POST':
        pass
    else:
        if request.session['token'] is None:
            return redirect('apps.accounts:login')
        else:
            token = request.session['token']
            return render(request, 'accounts/home.html')