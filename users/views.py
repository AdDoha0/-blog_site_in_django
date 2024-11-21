from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from users.forms import LoginUserForm




class LoginUser(LoginView):
    template_name = 'users/login.html'
    form_class = LoginUserForm

    def get_success_url(self):
        return reverse_lazy('all_posts')
