from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from users_api_service import login_user 

class CustomUserModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(username=username)
            # Verify the password using the external API
            response = login_user({'username': username, 'password': password})
            if response['status'] == 'success':  # Adjust this based on the actual API response
                return user
        except UserModel.DoesNotExist:
            return None

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None