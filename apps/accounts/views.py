from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from apps.accounts.lib import user as user_lib
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.urls import reverse

def logout_view(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('landing_page')) 

def register_view(request):
    msg = None
    success = False
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            result = user_lib.create_user(form.cleaned_data.get("email"),form.cleaned_data.get("email"),form.cleaned_data.get("password1"),"IN")
            if result:
                msg = 'User registration successful. Please click Sign In.'
                success = True
            else:
                msg = "A user already exists with provided email. Please choose another email."

        else:
            msg = 'There was problem with provided input. Please fix the errors and try again.'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("/app/")
            else:
                msg = 'Invalid credentials'
    else:
        return render(request, 'accounts/login.html')

def home_view(request):
    pass
    # if request.method == 'POST':
    #     pass
    # else:
    #     if request.session['token'] is None:
    #         return redirect('apps.accounts:login')
    #     else:
    #         token = request.session['token']
    #         return render(request, 'accounts/home.html')