from django.contrib.auth import authenticate, login
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from core.decorators import redirect_authenticated_user
from .forms import CustomLoginForm, RegisterForm, OtpForm
from .models import OtpCode
from .utils import send_activation_code
from random import randint

USER = get_user_model()

@redirect_authenticated_user
def login_view(request):
    error = None
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request, username=form.cleaned_data['username_or_email'], password=form.cleaned_data['password'])
            
            if user:
                if not user.is_active:
                    messages.warning(request, _(
                        f"ایمیل شما تایید نشده - {user.email}"))
                    return redirect('activate_email')
                else:
                    login(request, user)
                    return redirect('home:home')
            else:
                error = 'اطلاعات نامعتبر است'
    else:
        form = CustomLoginForm()
    return render(request, 'account/login.html', {'form': form, 'error': error})


@redirect_authenticated_user
def registeration_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save(True)

            code = randint(10000, 99999)
            otp = OtpCode(code=code, user=user)
            otp.save(True)
            try:
                send_activation_code(user.email, code)
            except:
                otp.delete()
                user.delete()
                messages.error(request, _('کد ارسال نشد'))
            else:
                request.session['email'] = user.email
                messages.success(
                    request, _(f'یک ایمیل تایید برای شما ارسال شد - {user.email}'))
                return redirect('activate_email')
    else:
        form = RegisterForm()
    return render(request, 'account/register.html', {'form': form})


@redirect_authenticated_user
def check_otp_view(request):
    email = request.session.get('email')
    if not email:
        return redirect('register')
    try:
        user = USER.objects.get(email=email)
    except USER.DoesNotExist:
        return redirect('register')
        
    if request.method == 'POST':
        form = OtpForm(request.POST)
        if form.is_valid():
            otp = OtpCode.objects.get(code=form.cleaned_data['otp'])
            user = otp.user
            otp.delete()
            user.is_active = True
            user.save()
            return redirect('login')
    else:
        form = OtpForm()
    return render(request, 'account/user_otp.html', {'form': form})

@redirect_authenticated_user
def resend_otp_view(request):
    email = request.session.get('email')
    if not email:
        return redirect('register')
    try:
        user = USER.objects.get(email=email)
    except USER.DoesNotExist:
        return redirect('register')
    code = randint(1000, 9999)        
    otp = OtpCode(code=code, user=user)
    otp.save(True)
    try:
        send_activation_code(user.email, code)
    except:
        otp.delete()
        messages.error(request, _('کد ارسال نشد'))
    else:
        messages.success(
            request, _(f'یک کد تایید برای شما ارسال شد - {user.email}')
        )
        return redirect('check_otp')
    

@redirect_authenticated_user
def check_reset_otp_view(request):
    if request.method == 'POST':
        form = OtpForm(request.POST)
        if form.is_valid():
            otp = OtpCode.objects.get(code=form.cleaned_data['otp'])
            request.session['email'] = otp.user.email
            messages.success(request, _(
                "یک رمز عبور وارد کنید"))
            return redirect('reset_new_password')
    else:
        form = OtpForm()
    return render(request, 'account/user_otp.html', {'form': form})


def change_email_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        if email:
            request.session['email'] = email
            return redirect('check_otp')
    return render(request, 'account/change_email.html')

