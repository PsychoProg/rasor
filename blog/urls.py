from django.urls import path 
from . import views

app_name = 'blog'

urlpatterns = [
     path('test/', views.testview, name='test'),
]
