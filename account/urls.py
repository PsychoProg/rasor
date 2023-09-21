from django.urls import path
from django.contrib.auth import views as auth_views
from . import views 



urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.registeration_view, name='register'),
    path('reset-code/', views.check_reset_otp_view, name='reset_code'),
    path('resend-code/', views.resend_otp_view, name='resend_otp_code'),
    path('check-otp/', views.check_otp_view, name='check_otp'),
    path('change-email/', views.change_email_view, name='change_email'),

    path('activate-email/', views.check_otp_view, name='activate_email'),
    # path("login/", views.MyLoginView.as_view(), name='login'),
    # path('register/', views.RegisterView.as_view(), name='register'),

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
