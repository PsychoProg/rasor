from django.urls import path 
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:pk>/<slug:slug>', views.product_detail, name='product_detail'),
    # path('cart-detail', views.CartDetailView.as_view(), name='cart_detail'),
    # path('cart-add', views.CartAddView.as_view(), name='cart_add'),
    # path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
]

# cart urls
urlpatterns += [
    path('add/<int:id>/', views.cart_add, name='cart_add'),
    path('item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart-detail/',views.cart_detail,name='cart_detail'),
]