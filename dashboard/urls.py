from django.urls import path 
from . import views 

app_name='dashboard'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('update-profile/', views.update_profile, name='update-profile'),
    path('contact/', views.contact_view, name="contact-us"),
]
