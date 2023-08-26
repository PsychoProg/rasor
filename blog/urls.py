from django.urls import path 
from . import views

app_name = 'blog'

urlpatterns = [
     path('products/', views.product_list, name='products_list'),
     path('test/', views.testview, name='test'),
]
