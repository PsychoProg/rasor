from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Count 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views import View
import requests
import json
from taggit.models import Tag 
from .models import Product, Order, OrderItem
from .cart import Cart
from home.models import ShareLinks


# =================================== Product LIST and DETAIL Views =================================== 
def product_list(request):
    prodcuts = Product.published.all()
    links = ShareLinks.objects.all()
    context = {
        'items': prodcuts,
        'links': links,
    }
    return render(request, 'home/list.html', context)


def product_detail(request, pk, slug):
    product = get_object_or_404(Product, id=pk, slug=slug)
    tags = product.tags.values_list('id', flat=True)
    similar_products = Product.published.filter(tags__in=tags).exclude(id=pk, slug=slug)
    similar_products = similar_products.annotate(tags_count=Count('tags')).order_by('-created_at')[:4]
    links = ShareLinks.objects.all()
    context = {
        'title': product.name,
        'items': product,
        'product_true': True,
        'similar_items': similar_products,
        'links': links,
    }
    return render(request, 'home/detail.html', context)


# =================================== Cart Views =================================== 
@login_required
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("product:cart_detail")


@login_required
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("product:cart_detail")


@login_required
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("product:cart_detail")

@login_required
def cart_detail(request):
    cart = Cart(request)
    context = {'cart': cart}
    return render(request, 'dashboard/cart_detail.html', context)

# =================================== Order Views =================================== 
@login_required
def create_order(request):
    cart = Cart(request)
    # create order for current user
    # create order items from cart session
    if cart.total() > 0:
        order = Order.objects.create(user=request.user, price=cart.total())
        for item in cart:
            OrderItem.objects.create(order=order, product=item['product'], price=item['price'])
    else:
        # if cart was empty redirect to cart detail 
        return redirect('product:cart_detail')
    
    cart.clear()
    return redirect('product:order_detail', order.id)

@login_required
def order_detail(request, pk=None):
    order = get_object_or_404(Order, id=pk)
    context = {'order': order}
    # order.items.all >> in template
    return render(request, 'dashboard/order_detail.html', context)


# =================================== Zarin Pal Views =================================== 
#? sandbox merchant 
if settings.SANDBOX:
    sandbox = 'sandbox'
else:
    sandbox = 'www'


ZP_API_REQUEST = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
ZP_API_STARTPAY = f"https://{sandbox}.zarinpal.com/pg/StartPay/"

amount = 1000  # Rial / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
# Important: need to edit for realy server.
CallbackURL = 'http://127.0.0.1:8080/product/verify/'


class SendRequestView(View):
    def post(self, request, pk):
        order = get_object_or_404(Order, id=pk, user=request.user)
        request.session['order_id'] = str(order.id)
        data = {
            "MerchantID": settings.MERCHANT,
            "Amount": order.price, # total price
            "Description": description,
            "Phone": request.user.phone,
            "CallbackURL": CallbackURL,
        }
        data = json.dumps(data)
        # set content length by data
        headers = {'content-type': 'application/json', 'content-length': str(len(data)) }
        try:
            response = requests.post(ZP_API_REQUEST, data=data,headers=headers, timeout=10)

            if response.status_code == 200:
                response = response.json()
                if response['Status'] == 100:
                    return {'status': True, 'url': ZP_API_STARTPAY + str(response['Authority']), 'authority': response['Authority']}
                else:
                    return {'status': False, 'code': str(response['Status'])}
            return response
        
        except requests.exceptions.Timeout:
            return {'status': False, 'code': 'timeout'}
        except requests.exceptions.ConnectionError:
            return {'status': False, 'code': 'connection error'}

def verify(request, authority):
    order_id = request.session['order_id']
    order = Order.objects.get(id=int(order_id))
    data = {
        "MerchantID": settings.MERCHANT,
        "Amount": order.price,
        "Authority": authority,
    }
    data = json.dumps(data)
    # set content length by data
    headers = {'content-type': 'application/json', 'content-length': str(len(data)) }
    response = requests.post(ZP_API_VERIFY, data=data,headers=headers)

    if response.status_code == 200:
        response = response.json()
        if response['Status'] == 100:
            return {'status': True, 'RefID': response['RefID']}
        else:
            return {'status': False, 'code': str(response['Status'])}
    return response

