from django.shortcuts import redirect
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.http import Http404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import user_passes_test
from functools import wraps

USER = get_user_model()


def redirect_authenticated_user(view, redirect_to='home:home'):
    @wraps(view)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(redirect_to)
        else:
            return view(request, *args, **kwargs)
    return wrapper


def only_authenticated_user(view, redirect_to='login'):
    @wraps(view)
    def wrapper(request, *args, **kwargs):
        if request.user.is_anonymous:
            return redirect(redirect_to)
        else:
            return view(request, *args, **kwargs)
    return wrapper


def mentor_required(function=None, redirect_field_name=None, login_url='home:home') :
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.profiles.is_mentor,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

 
    # return USER.is_active and USER.profiles.is_mentor 


"""

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import user_passes_test

def is_admin_or_student(user):
    return user.is_staff or user.userprofile.is_student

def home(request):
    return render(request, 'home.html')

@login_required
@user_passes_test(is_admin_or_student)
def restricted_home(request):
    return render(request, 'restricted_home.html')
"""