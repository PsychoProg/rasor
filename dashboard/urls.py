from django.urls import path 
from . import views 

app_name='dashboard'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('personal-info/', views.personal_info, name='personal-info'),
    path('update-profile/', views.update_profile, name='update-profile'),
]
