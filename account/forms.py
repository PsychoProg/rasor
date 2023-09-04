from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import validate_email
from django.contrib.auth import get_user_model
from django.forms import widgets
from django import forms
from .models import OtpCode

USER = get_user_model()

class CustomLoginForm(forms.Form):
    username_or_email = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username_or_email(self):
        username_or_email = self.cleaned_data['username_or_email']
        if "@" in username_or_email:
            validate_email(username_or_email)
            data = {'email': username_or_email}
        else:
            data = {'username': username_or_email}
        try:
            USER.objects.get(**data)
        except USER.DoesNotExist:
            raise ValidationError(
                _('این {} موجود نیست'.format(list(data.keys())[0])))
        else:
            return username_or_email

class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget = widgets.TextInput(
            attrs={'placeholder': "نام کاربری", "class": "form-control text-right"})
        # self.fields['first_name'].widget = widgets.TextInput(
        #     attrs={'placeholder': "نام", "class": "form-control text-right"})
        # self.fields['last_name'].widget = widgets.TextInput(
        #     attrs={'placeholder': "نام خانوادگی", "class": "form-control text-right"})
        self.fields['email'].widget = widgets.EmailInput(
            attrs={'placeholder': "ایمیل", "class": "form-control text-right"})
        self.fields['password1'].widget = widgets.PasswordInput(
            attrs={'placeholder': "رمز عبور", "class": "form-control text-right"})
        self.fields['password2'].widget = widgets.PasswordInput(
            attrs={'placeholder': "تکرار رمز عبور", "class": "form-control text-right"})

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = USER.objects.filter(username__iexact=username)
        if qs.exists():
            raise forms.ValidationError("این نام کاربری نامعتبر است")
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = USER.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("ایمیل نامعتبر است")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError("رمز عبور هخوانی ندارد")
        if password1 and password2 and password1 == password2:
            if len(password1) <= 8 or len(password1) > 40:
                raise forms.ValidationError("تعداد کاراکترهای رمز عبور مناسب نیست")
        return password2

    class Meta:
        model = USER
        fields = ("username", "email", "first_name", "last_name")



class OtpForm(forms.Form):
    otp = forms.CharField(widget=forms.TextInput)

    def clean_otp(self):
        otp_code = self.cleaned_data['otp']
        try:
            OtpCode.objects.get(code=otp_code)
        except OtpCode.DoesNotExist:
            raise ValidationError(
                _('کد وارد شده معتبر نیست')
            )
        else:
            return otp_code
