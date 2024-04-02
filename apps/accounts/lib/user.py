from django.contrib.auth.models import User
from apps.accounts.actions import user as user_actions
from django.contrib.auth import authenticate

def create_user(email:str,username,password,country)->bool:
    """
    A function to create a user with the given email, username, password, and country.
    
    Parameters:
    - email (str): The email of the user.
    - username (str): The username of the user.
    - password: The password of the user.
    - country: The country of the user.
    
    Returns:
    - bool: True if the user was successfully created, False otherwise.
    """
    result=False
    qs = User.objects.filter(email=email)
    if qs.count() == 0:
        username = username
        raw_password = password
        country = country
        user = user_actions.do_create_user(username=username, password=raw_password, email=email, country=country)
        if user is not None:
            user = authenticate(username=username, password=raw_password)
            result = True
    return result