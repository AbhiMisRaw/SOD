from django.db import transaction
from django.shortcuts import render, redirect
from core.users_api_service import register_user, login_user, logout_user, update_user,search_user_response
from django.contrib import messages
from apps.accounts.actions.user_profile import do_create_user_profile
from typing import Optional
from apps.accounts.models import UserProfile

def get_or_create_user(username, password):
    data={}
    data["username"] = username
    response = search_user_response(data)
    if response.status_code == 200:
        users_list = response.json().get('users')
        if len(users_list) > 0:
            user_id = users_list[0].get('id')
            return user_id
        else:
            pass
    elif response.status_code == 404:
        return do_create_user(username, password)
    else:
        return None


def do_update_user(
    user_id,
    data,
) -> UserProfile:
    result = False
    with transaction.atomic():
        response = update_user(user_id, data)
        if response.status_code == 200:
            result = True
        else:
            result = False
    return result

def do_create_user(username,password):
    data = {}
    data["username"] = username
    data["password"] = password
    # data = {
    #         'username': username,
    #         'password': password,
    #                 }
    response = register_user(data)
    if response.status_code == 201:
        user_id = response.json().get('user_id')
    elif response.status_code == 400:
        user_id = None

    return user_id

