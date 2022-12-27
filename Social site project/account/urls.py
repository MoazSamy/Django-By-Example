from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # This is the function defined view
    # path("login/", views.user_login, name="login"),
    # These are the CBV from django
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]