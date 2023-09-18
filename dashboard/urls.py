from django.urls import path 
from . import views 

app_name='dashboard'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('update-profile/', views.update_profile, name='update_profile'),
    path('contact/', views.contact_view, name='contact_us'),
    path('course/create', views.create_course, name='create_course'),
    path('course/detail/<int:course_id>', views.course_detail, name='course_detail'),
    path('course/content/<int:course_id>', views.course_content, name='course_content'),
    path('course/list', views.course_list, name='course_list'),

]
