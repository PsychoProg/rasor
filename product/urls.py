from django.urls import path 
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.product_list, name='products_list'),
    path('<int:pk>/<slug:slug>', views.product_detail, name='products_detail'),
]