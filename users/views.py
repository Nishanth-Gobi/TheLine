from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .forms import UserCreateForm
from django.contrib.auth import views as auth_views


class UserRegisterView(generic.CreateView):
    form_class = UserCreateForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserLoginView(auth_views.LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('home')
