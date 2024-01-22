from apps.accounts.models import UserProfile
from typing import Optional

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