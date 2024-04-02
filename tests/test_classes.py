import pytest
from django.contrib.auth.models import User


@pytest.mark.django_db
class BaseTest:

    @pytest.fixture
    def user(self):
        user_obj={}
        test_email = "test@mail.com"
        test_password = "Andy@99"
        user_obj["username"] = test_email
        user_obj["password"] = test_password
        yield user_obj


    # @pytest.fixture
    # def user_profile(self,user):
    #     test_email = user["username"]
    #     test_password = user["password"]
    #     user_id=user_actions.get_or_create_user(test_email, test_password)
    #     user_profile = user_profile_actions.get_or_create_user_profile(user_id)
    #     yield user_profile
    #     user_profile.delete()
################################################################################################################################
# Client
################################################################################################################################

    def user_login(self,client,user_profile):
        client.force_login(user_profile) 

    

################################################################################################################################
# Users
################################################################################################################################

    def initialize_user(self,user:User,is_superuser:bool,is_staff:bool,is_active:bool):
        user.is_superuser = is_superuser
        user.is_staff = is_staff
        user.is_active = is_active
        user.save()