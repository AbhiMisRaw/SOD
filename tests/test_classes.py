import pytest
from apps.accounts.actions import user as user_actions

@pytest.mark.django_db
class BaseTest:
    @pytest.fixture
    def user(self):
        country = "IN"
        user = user_actions.do_create_user("Test@mail.com", "Test@123",country)
        yield user
        user.delete()
