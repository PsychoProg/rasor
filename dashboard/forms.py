from django import forms 
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm

USER = get_user_model()

class ProfileUpdateForm(UserChangeForm):
    class Meta:
        model = USER
        fields = ['username', 'email', 'phone', 'address', 'picture', 'first_name', 'last_name']
    username = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control text-right', 
        'placeholder':"نام کاربری" }))
    
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'type': 'email', 'class': 'form-control text-right',
        'placeholder':"ایمیل"  }))

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control text-right', 
        'placeholder':"نام" }))

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control text-right', 
        'placeholder':"نام خانوادگی" }))

    phone = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control text-right', 
        'placeholder':"تلفن همراه" }))

    address = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control text-right', 
        'placeholder':"آدرس" }))

    # picture = forms.ImageField()

