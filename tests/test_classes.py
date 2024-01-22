import pytest
from apps.accounts.actions import user as user_actions
from apps.accounts.models import UserProfile
from core.users_api_service import login_user, logout_user, register_user


@pytest.mark.django_db
class BaseTest:
    @pytest.fixture
    def user(self):
        country = "IN"
        user = user_actions.do_create_user("Test@mail.com", "Test@123",country)
        yield user
        user.delete()
################################################################################################################################
# Client
################################################################################################################################

    def user_login(self,client,user):
        client.force_login(user)    

################################################################################################################################
# Users
################################################################################################################################

    def initialize_user(self,user:UserProfile,is_superuser:bool,is_staff:bool,is_active:bool):
        data={}
        data["is_superuser"] = is_superuser
        data["is_staff"] = is_staff
        data["is_active"] = is_active
        
        user_id = user.user_id
        response = user_actions.update_user(user_id,data)