from django.urls import path
from .views import UserRegisterView, UserLoginView, UserEditView, PasswordEditView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', UserLoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('register/', UserRegisterView.as_view(), name="register"),
    path('edit_profile/', UserEditView.as_view(), name="edit_profile"),
    path('password/', PasswordEditView.as_view(), name="password"),
    # path('password-success/', PasswordSuccess.as_view(), name="password_success"),

]
