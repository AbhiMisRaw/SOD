from django.db import transaction
from django.shortcuts import render, redirect
from core.users_api_service import register_user, login_user, logout_user
from django.contrib import messages
from apps.accounts.actions.user_profile import do_create_user_profile
from typing import Optional
from apps.accounts.models import UserProfile

def do_create_user(
    username: Optional[str] = None,
    password: Optional[str] = None,
    country: Optional[str] = None,
) -> UserProfile:
    user_profile = None
    with transaction.atomic():
        data = {
            'username': username,
            'password': password,
                    }
        response = register_user(data)
        if response.status_code == 201:
            user_id = response.json().get('user_id')
            user_profile = do_create_user_profile(user_id=user_id, country="IN")
        elif response.status_code == 400:
            user_profile = None

    return user_profile