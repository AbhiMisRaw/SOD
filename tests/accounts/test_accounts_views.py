from tests.test_classes import BaseTest
from django.urls import reverse
from apps.accounts.actions import user as user_actions, user_profile as user_profile_actions
from tests.lib import utils

class Test_Auth_Register_View(BaseTest):
    def test_register_user_view_get(self,client):
        response = client.get(reverse('apps.accounts:register'))
        assert response.status_code == 200
    
    def test_register_user_view_get_template(self,client):
        response = client.get(reverse('apps.accounts:register'))
        assert response.status_code == 200
        assert 'accounts/register.html' in [t.name for t in response.templates]
    
    def test_register_user_view_post_success(self,client):
        email = utils.generate_random_email()
        password = 'testpass123'
        #country = "IN"
        data = {
            'email': email,
            'password1': password,
            'password2': password
        }
        response = client.post(reverse('apps.accounts:register'), data=data)
        assert response.status_code == 200
        assert user_actions.is_user_created(email) == True
        assert user_profile_actions.is_user_profile_created(email) == True
        assert response.context['success']
        assert response.context['msg'] == 'User registration successful. Please click Sign In.'

    def test_register_user_view_post_invalid(self,client):
        #country = "ABC"
        data = {
            'email': 'invalidemail',
            'password1': 'testpass123',
            'password2': 'testpass456',
        }
        response = client.post(reverse('apps.accounts:register'), data=data)
        assert response.status_code == 200
        assert 'There was problem with provided input. Please fix the errors and try again.' in response.context['msg']
        assert not response.context['success']
    
    def test_register_user_view_post_invalid_email(self,client):
        data = {
            'email': 'invalidemail',
            'password1': 'testpass123',
            'password2': 'testpass123',
        }
        response = client.post(reverse('apps.accounts:register'), data=data)
        assert response.status_code == 200
        assert 'There was problem with provided input. Please fix the errors and try again.' in str(response.content)

    def test_register_user_view_post_mismatched_passwords(self,client):
        data = {
            'email': 'test@example.com',
            'password1': 'testpass123',
            'password2': 'testpass456',
        }
        response = client.post(reverse('apps.accounts:register'), data=data)
        assert response.status_code == 200
        assert 'There was problem with provided input. Please fix the errors and try again.' in str(response.content)

    def test_register_user_view_post_invalid_existing_email(self,client,user):
        email = utils.generate_random_email()
        password = 'testpass123'
        #country = "IN"
        data = {
            'email': email,
            'password1': password,
            'password2': password,
        }
        response = client.post(reverse('apps.accounts:register'), data=data)
        password = 'testpass123'
        #country = "IN"
        data = {
            'email': email,
            'password1': password,
            'password2': password
        }
        response = client.post(reverse('apps.accounts:register'), data=data)
        assert response.status_code == 200
        assert 'A user already exists with provided email. Please choose another email.' in response.context['msg']
        assert not response.context['success']