from django.urls import path
from .views import UserRegisterView, UserLoginView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', UserLoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('register/', UserRegisterView.as_view(), name="register"),

]
