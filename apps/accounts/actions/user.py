
from django.contrib.auth.models import User
from typing import Optional
from django.db import transaction

def do_create_user(
    username: Optional[str] = None,
    password: Optional[str] = None,
    country: Optional[str] = None,
    email: Optional[str] = None,
    bio: Optional[str] = None,
) -> User:
    with transaction.atomic():
        user = User.objects.create_user(
            username = username,
            password = password,
            email = email
        )
    return user