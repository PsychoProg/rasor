from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views import View
from .forms import ProfileUpdateForm

USER = get_user_model()


@login_required
def dashboard(request):
    return render(request, 'dashboard/base.html')
        

@login_required
def update_profile(request):
    """ update user profile """
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, request.FILES ,instance=request.user)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'پروفایل شما با موفقیت اپدیت شد')
            return redirect('dashboard:dashboard')
    else:
        form = ProfileUpdateForm(instance=request.user)

    context = {
        'form': form,
        'title': 'اطلاعات شخصی'
    }
    return render(request, 'dashboard/update-profile.html', context)

