from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views import View
from .forms import ProfileUpdateForm, UserUpdateForm
from account.models import Profile

USER = get_user_model()


@login_required
def dashboard(request):
    return render(request, 'dashboard/base.html')


def return_degree(value):
    if value == 'PHD':
        return 'دکتری'
    elif value == 'Postgraduated':
        return 'کارشناسی ارشد'
    elif value == 'undergraduated':
        return 'کارشناسی'
    elif value == 'Associate of art':
        return 'کاردانی'
    elif value == 'associate of science':
        return 'دیپلم علوم تجربی'
    elif value == 'associate of liberal arts':
        return 'دیپلم علوم انسانی'
    elif value == 'associate of math':
        return 'دیپلم علوم ریاضی'
        

@login_required
def personal_info(request):
    form = ProfileUpdateForm()
    user = request.user.username
    user = USER.objects.filter(username=user)
    profile = get_object_or_404(Profile, user=request.user)
    degree = return_degree(profile.degree)
    context = {
        'profile': profile,
        'degree': degree,
        'form': form,
        'title': 'اطلاعات شخصی'
    }
    return render(request,'dashboard/personal-info.html', context)


@login_required
def update_profile(request):
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, instance=request.user)

        # if user_form.is_valid() and profile_form.is_valid():
        if user_form.is_valid():
            user_form.save()
            # profile_form.save()
            messages.success(request, 'پروفایل شما با موفقیت اپدیت شد')
            return redirect('dashboard:dashboard')
    
    user_form = UserUpdateForm(instance=request.user)
    profile_form = ProfileUpdateForm(instance=request.user)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'title': 'بروزرسانی اطلاعات'
    }
    return render(request, 'dashboard/update-profile.html', context)

