from apps.accounts.models import UserProfile
from typing import Optional

from core.users_api_service import search_user_response

def is_user_profile_created(username: str) -> bool:
    data = {}
    data["username"] = username
    result = False
    response = search_user_response(data)
    if response.status_code == 200:
        users_list = response.json().get('users')
        if len(users_list) > 0:
            user = users_list[0]
            if user.get('username') == username:
                if user.get('id') != None:
                    user_id = user.get('id')
                    try:
                        UserProfile.objects.get(user_id=user_id)
                        result = True
                    except UserProfile.DoesNotExist:
                        result  = False
        else:
            result  = False
    elif response.status_code == 404:
        result  = False
    else:
        result  = False
    return result


def get_or_create_user_profile(user_id: int) -> UserProfile:
    user_profile = UserProfile.objects.get_or_create(user_id=user_id, country="IN",subscription_type = "F")[0]
    return user_profile

def do_create_user_profile(
    user_id: int,
    first_name: Optional[str] = None,
    last_name: Optional[str] = None,
    address: Optional[str] = None,
    bio: Optional[str] = None,
    country: Optional[str] = None,
) -> UserProfile:
    user_profile = UserProfile.objects.create(
        first_name=first_name,
        last_name=last_name,
        address=address,
        bio=bio,
        user_id=user_id,
        country=country,
        subscription_type = "F"
    )
    return user_profile

