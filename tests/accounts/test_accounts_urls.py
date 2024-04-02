from django.urls import reverse
import pytest
from tests.test_classes import BaseTest
from django.contrib.auth.views import PasswordChangeDoneView

@pytest.mark.django_db
class Test_Authentication_Urls(BaseTest):

    def test_view_auth_login(self,client):
        response = client.get(reverse("apps.accounts:login"))

        assert response.status_code == 200

    # def test_view_auth_logout(self,client,user,user_profile):
    #     self.initialize_user(user_profile,False,False,True)
    #     self.login_user(client, user)
    #     response = client.get(reverse("apps.accounts:logout"))

    #     assert response.status_code == 302

    def test_view_auth_register(self,client):
        response = client.get(reverse("apps.accounts:register"))
        assert response.status_code == 200