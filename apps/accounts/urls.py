from django.urls import path, include
from .views import register_view, login_view, logout_view
from django.contrib.auth.views import LogoutView

app_name = 'apps.accounts'

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_view, name="register"),
    path("logout/", logout_view, name="logout"),
    # path('logout/', logout_view, name="logout"),
]