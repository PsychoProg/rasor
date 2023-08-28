from django import forms
from django.contrib.auth.models import User 
from django.core import validators
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        super(UserRegisterForm, self).clean()
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password and password2 and password != password2:
            self._errors['password'] = self.error_class([
                'رمز عبور را دوباره وارد کنید'])
            
        if User.objects.filter(email=email).exists():
            self._errors['email'] = self.error_class([
                'ایمیل معتبر نیست'])
        
        if User.objects.filter(username=username).exists():
            self._errors['username'] = self.error_class([
                'نام کاربری معتبر نیست'])
        
        
    
    # def clean_password2(self):
    #     password = self.cleaned_data.get('password')
    #     password2 = self.cleaned_data.get('password2')
    #     if password and password2 and password != password2:
    #         self._errors['password'] = self.error_class([
    #             'رمز عبور را دوباره وارد کنید'])
    #     return password2

    # def clean_email(self):
    #     """ check if email exists """
    #     email = self.cleaned_data.get('email')
    #     if User.objects.filter(email=email).exists():
    #         self._errors['email'] = self.error_class([
    #             'ایمیل معتبر نیست'])
    #     return email 
    

class CheckOtpForm(forms.ModelForm):
    code = forms.CharField(
        widget=forms.TextInput, 
        validators=[validators.MaxLengthValidator(5)]
        )
