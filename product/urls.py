from django.urls import path 
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:pk>/<slug:slug>/', views.product_detail, name='product_detail'),

    # path('orders/<int:pk>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('checkout/', views.CheckoutView.as_view(), name='create_order'),
    path('order/<int:order_id>/delete/', views.clear_order, name='clear_order'),
    path('order/detail/<int:order_id>', views.order_detail, name='order_detail'),
    # path('order/add/', views.create_order, name='create_order'),
    
    path('apply/', views.apply, name="apply"), # delete for production
]

# Cart URLs
urlpatterns += [
    # path('add/<int:id>/', views.cart_add, name='cart_add'),
    # path('item_clear/<int:id>/', views.item_clear, name='item_clear'),  
    # path('cart/detail/',views.cart_detail,name='cart_detail'),      
    # path('cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/detail', views.CartView.as_view(), name='cart_detail'),
    path('add/', views.AddToCartView.as_view(), name='cart_add'),
    path('remove/', views.CartItemClear.as_view(), name='item_clear'),
    path('clear/', views.ClearCartView.as_view(), name='clear_cart'),
    path('print/', views.PrintCart.as_view(), name='print_cart'),
]

# ZarinPal
urlpatterns += [
    path('request/<int:pk>/', views.SendRequestView.as_view(), name='request'),
    path('verify/', views.verify , name='verify'),
]