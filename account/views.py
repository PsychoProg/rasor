from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.views import LoginView
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User 
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from rasor import settings
from uuid import uuid4
from random import randint
from .forms import UserRegisterForm, CheckOtpForm
from .models import Otp


class MyLoginView(LoginView):
    template_name = 'account/login.html'
    redirect_authenticated_user = True
    

class RegisterView(View):
    """ registeration view with OTP code """
    def get(self, request):
        form = UserRegisterForm()
        context = {'form': form}
        if request.user.is_authenticated:
            return redirect('home:home')
        return render(request, 'account/register.html', context)

    def post(slef, request):
        if request.user.is_authenticated:
            return redirect('home:home')
        form = UserRegisterForm(request.POST)
        context = {'form': form}
        if form.is_valid():

            form.save()
            return redirect('home:home') 

        return render(request, 'account/register.html', context)


class CheckOtpView(View):
    def get(self, request):
        form = CheckOtpForm()
        context = {'form': form}
        return render(request, 'account/check_otp.html', context)

    def post(self, request):
        # email = request.GET.get("email")
        token = request.GET.get("token")
        form = CheckOtpForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            cd = form.cleaned_data
            if Otp.objects.filter(token=token, pass_code=cd["code"]).exists():
                otp = Otp.objects.get(token=token)
                user, is_created = User.objects.get_or_create(email=otp.email)
                login(request, user)
                # delete OTP
                otp.delete()
                return redirect('/')
        else:
            form.add_error('email', 'invalid email!!!')

        return render(request, 'account/check_otp.html', context)
