from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import LoginUserForm, RegisterUserForm




class LoginUser(LoginView):
    template_name = 'users/login.html'
    form_class = LoginUserForm

    def get_success_url(self):
        return reverse_lazy('main:all_posts')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')