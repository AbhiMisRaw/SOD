from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import re
from apps.lib import constants

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control",
                "required":"",
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control form-icon-input",
                "id":"password",
                "required":"",

            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control form-icon-input",
                "id":"confirmPassword",
                "required":"",
            }
        ))
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')