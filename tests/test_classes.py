import pytest
from apps.accounts.actions import user as user_actions, user_profile as user_profile_actions
from apps.accounts.models import UserProfile
from core.users_api_service import login_user_response, logout_user, register_user,update_user,login_user


@pytest.mark.django_db
class BaseTest:

    @pytest.fixture
    def user(self):
        user_obj={}
        test_email = "test@mail.com"
        test_password = "Test@123"
        user_obj["username"] = test_email
        user_obj["password"] = test_password
        yield user_obj


    @pytest.fixture
    def user_profile(self,user):
        test_email = user["username"]
        test_password = user["password"]
        user_id=user_actions.get_or_create_user(test_email, test_password)
        user_profile = user_profile_actions.get_or_create_user_profile(user_id)
        yield user_profile
        user_profile.delete()
################################################################################################################################
# Client
################################################################################################################################

    def user_login(self,client,user_profile):
        client.force_login(user_profile) 

    def login_user(self,client,user):
        data = {
                'email': user["username"],
                'password': user["password"],
            }
        response = login_user(data)
        if response['status'] == 'success':
            session = client.session
            session['email'] = data['email']
            session['token'] = response.get('token')
            session.save()
        else:
            return None

################################################################################################################################
# Users
################################################################################################################################

    def initialize_user(self,user_profile:UserProfile,is_superuser:bool,is_staff:bool,is_active:bool):
        data={}
        data["is_superuser"] = is_superuser
        data["is_staff"] = is_staff
        data["is_active"] = is_active
        
        user_id = user_profile.user_id
        response = user_actions.do_update_user(user_id,data)