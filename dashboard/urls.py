from django.urls import path 
from . import views 

app_name='dashboard'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('update-profile/', views.update_profile, name='update_profile'),
    path('contact/', views.contact_view, name='contact_us'),
    path('create-course', views.create_course, name='create_course'),
]
