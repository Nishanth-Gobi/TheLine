from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .forms import UserCreateForm, UserEditForm, PasswordChangingForm
from django.contrib.auth import views as auth_views
# from django.contrib.auth.forms import PasswordChangeForm


class UserRegisterView(generic.CreateView):
    form_class = UserCreateForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserLoginView(auth_views.LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('home')


class UserEditView(generic.UpdateView):
    form_class = UserEditForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


class PasswordEditView(auth_views.PasswordChangeView):
    form_class = PasswordChangingForm
    template_name = 'registration/change-password.html'
    success_url = reverse_lazy('home')
