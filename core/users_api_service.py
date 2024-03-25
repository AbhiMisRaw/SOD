import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = 'http://127.0.0.1:7000/api/accounts/'

# ADMIN_USERNAME = os.getenv('DIARY_USERS_API_ADMIN_USERNAME')
# ADMIN_PASSWORD = os.getenv('DIARY_USERS_API_ADMIN_USERNAME')

ADMIN_USERNAME = "admin@mail.com"
ADMIN_PASSWORD = "Andy@99"

def update_user(user_id, data):
    # Login as admin
    admin_data = {
        'email': ADMIN_USERNAME,
        'password': ADMIN_PASSWORD,
    }
    login_response = requests.post(f'{BASE_URL}user/login/', data=admin_data)
    login_data = login_response.json()

    # Extract the token from the login response
    token = login_data.get('token')  # Adjust this based on the actual API response

    # Add the token to the headers for the registration request
    headers = {
        'Authorization': f'Token {token}',
    }

    response = requests.put(f'{BASE_URL}user/{user_id}/update/', data=data, headers=headers)
    return response

def search_user_response(data):
    # Login as admin
    admin_data = {
        'email': ADMIN_USERNAME,
        'password': ADMIN_PASSWORD,
    }
    login_response = requests.post(f'{BASE_URL}user/login/', data=admin_data)
    login_data = login_response.json()

    # Extract the token from the login response
    token = login_data.get('token')  # Adjust this based on the actual API response

    # Add the token to the headers for the registration request
    headers = {
        'Authorization': f'Token {token}',
    }

    response = requests.post(f'{BASE_URL}users/search/', data=data, headers=headers)
    return response

def register_user(data):
    # Login as admin
    admin_data = {
        'email': ADMIN_USERNAME,
        'password': ADMIN_PASSWORD,
    }
    login_response = requests.post(f'{BASE_URL}user/login/', data=admin_data)
    login_data = login_response.json()

    # Extract the token from the login response
    token = login_data.get('token')  # Adjust this based on the actual API response

    # Add the token to the headers for the registration request
    headers = {
        'Authorization': f'Token {token}',
    }

    response = requests.post(f'{BASE_URL}user/register/', data=data, headers=headers)
    return response

def login_user(data):
    response = requests.post(f'{BASE_URL}user/login/', data=data)
    return response.json()

def login_user_response(data):
    response = requests.post(f'{BASE_URL}user/login/', data=data)
    return response

def logout_user(data):
    
    # Extract the token from the login response
    token = data["token"] # Adjust this based on the actual API response

    # Add the token to the headers for the logout request
    headers = {
        'Authorization': f'Token {token}',
    }

    response = requests.post(f'{BASE_URL}user/logout/', headers=headers)
    return response
