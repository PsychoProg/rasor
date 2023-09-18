from django.shortcuts import redirect
from django.conf import settings
from .models import Order, OrderItem, Product


class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def unique_id_generator(self, id):
        unique = f'{id}'
        return unique

    def __iter__(self):
        """ adding items to cart values """
        cart = self.cart.copy()
        for item in cart.values():
            item['product'] = Product.objects.get(id=int(item['product_id']))
            item['total'] = int(item['price'])
            yield item 

    def add(self, product):
        unique = self.unique_id_generator(product.id)
        if unique not in self.cart:
            self.cart[unique] = {
                'user_id': self.request.user.id,
                'product_id': product.id,
                'name': product.name,
                'price': int(product.price),
            }
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True
    
    def total(self):
        cart = self.cart.values()
        total = sum(int(item['price']) for item in cart)
        return total 
    
    def remove(self, product):
        """ remove items """
        unique = self.unique_id_generator(product.id)
        if unique in self.cart:
            del self.cart[unique]
            self.save()

    def clear(self):
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True