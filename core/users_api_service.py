import requests

BASE_URL = 'http://127.0.0.1:7000/api/accounts/'
ADMIN_USERNAME = "admin@mail.com"
ADMIN_PASSWORD = "Test@123"

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
    return response.json()

def login_user(data):
    response = requests.post(f'{BASE_URL}user/login/', data=data)
    return response.json()

def logout_user(data):
    
    # Extract the token from the login response
    token = data["token"] # Adjust this based on the actual API response

    # Add the token to the headers for the logout request
    headers = {
        'Authorization': f'Token {token}',
    }

    response = requests.post(f'{BASE_URL}user/logout/', headers=headers)
    return response
