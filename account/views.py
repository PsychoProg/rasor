from django.shortcuts import render
from django.contrib.auth.views import LoginView


class MyLoginView(LoginView):
    template_name = 'account/login.html'
    redirect_authenticated_user = True
    
