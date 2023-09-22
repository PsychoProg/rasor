from django import forms 
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm
from django.forms import widgets
from .models import Comments, Course, CourseContent, CourseMessage

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


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        self.fields['subject'].widget = widgets.TextInput(
            attrs={'placeholder': 'موضوع', 'class': 'form-control text-right'}
        )
        self.fields['message'].widget = widgets.Textarea(
            attrs={'placeholder': 'پیام خود را بنویسید', 'class': 'form-control text-right'}
        )

    class Meta:
        model = Comments
        fields = ['subject', 'message']


class CourseCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CourseCreateForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget = widgets.TextInput(
            attrs={'placeholder': 'نام دوره', 'class':'form-control text-right'}
        )
        self.fields['description'].widget = widgets.Textarea(
            attrs={'placeholder': 'توضیحات', 'class':'form-control text-right'}
        )
        self.fields['price'].widget = widgets.TextInput(
            attrs={'placeholder': 'قیمت (ریال)', 'class':'form-control text-right'}
        )

    class Meta:
        model = Course
        fields = ['title', 'description', 'image', 'price']


class CourseContentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CourseContentForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget = widgets.TextInput(
            attrs={'placeholder': 'عنوان فایل', 'class':'form-control text-right'}
        )

    class Meta:
        model = CourseContent
        # fields = ['course', 'title', 'file']
        fields = ['title', 'file']

class MessageForm(forms.ModelForm):
    class Meta:
        model = CourseMessage
        fields = ['content']

    content = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control text-right', 
        'placeholder':"پیام خود را وارد کنید" }))