from django.urls import path
from django.contrib.auth import views as auth_views
from . import views 



urlpatterns = [
    path("login/", views.MyLoginView.as_view(), name='login'),
    # path("login/", auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('check-otp', views.CheckOtpView.as_view(), name='check_otp_url'),
    path("logout/", auth_views.LogoutView.as_view(template_name='account/logout.html'), name="logout"),
    path(
        "password_change/", 
        auth_views.PasswordChangeView.as_view(template_name='account/password_change.html'),
        name="password_change"
    ),
    path(
        "password_change/done/",
        auth_views.PasswordChangeDoneView.as_view(template_name='account/password_change_done.html'),
        name="password_change_done",
    ),
    path(
        "password_reset/",
        auth_views.PasswordResetView.as_view(template_name='account/password_reset.html'), 
        name="password_reset"),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html'),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'),
        name="password_reset_complete",
    ),
]
