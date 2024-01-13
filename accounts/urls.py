from django.urls import path, include
from .views import  register_view, login_view, home_view

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_view, name="register"),
    path('home/', home_view, name="home"),
]