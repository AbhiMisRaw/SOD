from tests.test_classes import BaseTest
from django.urls import reverse

class Test_Auth_Register_View(BaseTest):
    def test_register_user_view_get(self,client):
        response = client.get(reverse('apps.accounts:register'))
        assert response.status_code == 200