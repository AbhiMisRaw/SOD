from django.http import HttpResponse
from django.shortcuts import render
from .forms import SignUpForm, LoginForm
from apps.accounts.lib import user as user_lib
from django.contrib.auth import authenticate


# def logout_view(request):
#     data = {}
#     data['token'] = request.session['token']
#     logout_user(data)
#     request.session['token'] = None
#     return redirect('/')

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
                msg = "User with provided email already exists. Please choose another email"

        else:
            msg = 'Provided data is not valid'
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
            return HttpResponse("Welcome user")
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