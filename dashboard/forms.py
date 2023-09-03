from django import forms 
from django.contrib.auth import get_user_model 
from account.models import Profile


USER = get_user_model()


class ProfileUpdateForm(forms.ModelForm):
    phone = forms.CharField(
        widget=forms.TextInput(attrs={
            'type': 'text', 'class': 'form-control text-right', 'placeholder': 'تلفن همراه'}))

    address = forms.CharField(
        widget=forms.TextInput(attrs={
            'type': 'text', 'class': 'form-control text-right', 'placeholder': 'آدرس' }))

    image = forms.ImageField(widget=forms.FileInput)

    class Meta:
        model = Profile
        fields = ['phone', 'degree', 'address', 'image'] # image


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'type': 'text', 'class': 'form-control text-right', 'placeholder': 'نام کاربری'}))
    
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'type': 'text', 'class': 'form-control has-feedback-left text-right', 'placeholder': 'نام'}))
    
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'type': 'text', 'class': 'form-control text-right', 'placeholder': 'نام خانوادگی' }))

    email = forms.EmailField(
        widget=forms.TextInput(attrs={
            'type': 'email', 'class': 'form-control has-feedback-left text-right', 'placeholder': 'ایمیل' }))
    
    class Meta:
        model = USER 
        fields = ['username', 'first_name', 'last_name', 'email']