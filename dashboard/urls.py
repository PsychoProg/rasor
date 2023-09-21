from django.urls import path 
from . import views 

app_name='dashboard'

# profile urls
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('update-profile/', views.update_profile, name='update_profile'),
    path('contact/', views.contact_view, name='contact_us'),

]

# course urls
urlpatterns += [
    path('course/list/all', views.all_course_list, name='all_course_list'),
    path('course/list', views.course_list, name='course_list'),
    path('course/create', views.create_course, name='create_course'),
    path('course/detail/<int:course_id>', views.course_detail, name='course_detail'),
    path('course/content/<int:course_id>', views.course_content, name='course_content'),
    path('course/<int:course_id>/message/', views.create_message, name="create_message"),

]
