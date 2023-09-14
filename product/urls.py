from django.urls import path 
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:pk>/<slug:slug>', views.product_detail, name='product_detail'),
    path('order/detail/<int:pk>', views.order_detail, name='order_detail'),
    path('order/add', views.create_order, name='create_order'),
]

# Cart URLs
urlpatterns += [
    path('add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/detail/',views.cart_detail,name='cart_detail'),      
    path('item_clear/<int:id>/', views.item_clear, name='item_clear'),  
]