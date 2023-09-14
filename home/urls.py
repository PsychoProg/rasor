from django.urls import path 
from . import views 

app_name = 'home'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('news/<int:pk>/<slug:slug>/', views.news_detail, name='news_detail'),
    path('news-list', views.news_list, name='news_list'),
    path('about-us', views.about_view, name='about_us'),
]
