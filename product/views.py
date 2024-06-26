from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Count 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic import TemplateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import CartMixin
import requests
import json
from taggit.models import Tag 
from .models import Product, Order, OrderItem
from dashboard.models import Course
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
        'title': product.title,
        'items': product,
        'product_true': True,
        'similar_items': similar_products,
        'links': links,
    }
    return render(request, 'home/detail.html', context)


# =================================== Cart Views =================================== 
class AddToCartView(LoginRequiredMixin, CartMixin, TemplateView):
    template_name='dashboard/cart_detail.html'
    def post(self, request, *args, **kwargs):
        cart = self.get_cart()
        id = request.POST.get('id')
        type = request.POST.get('type')
        if type == 'product':
            product = get_object_or_404(Product, id=id)
        elif type == 'course':
            product = get_object_or_404(Course, id=id)
        else:
            return redirect('product:cart_detail')
        cart.add(product=product, type=type)
        return redirect('product:cart_detail')


class CartItemClear(LoginRequiredMixin, CartMixin, TemplateView):
    template_name='dashboard/remove_from_cart.html'
    def post(self, request, *args, **kwargs):
        cart = self.get_cart()
        unique = request.POST.get('unique_id')
        cart.remove(unique)
        return redirect('product:cart_detail')


class ClearCartView(LoginRequiredMixin, CartMixin, TemplateView):
    template_name='dashboard/cart_detail.html'
    def post(self, request, *args, **kwargs):
        cart = self.get_cart()
        cart.clear()
        return redirect('product:cart_detail')

class PrintCart(LoginRequiredMixin, CartMixin, TemplateView):
    template_name='dashboard/cart_detail.html'
    def post(self, request,*args,**kwargs):
        cart = self.get_cart()
        print('*'*30)
        print(cart)
        return redirect('product:cart_detail')


class CartView(CartMixin, TemplateView, LoginRequiredMixin):
    template_name='dashboard/cart_detail.html'

# =================================== Order Views =================================== 
@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    context = {'order': order}
    # order.items.all >> in template
    return render(request, 'dashboard/order_detail.html', context)


@login_required
def clear_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if request.method == 'POST':
        order.delete()
        return redirect('product:cart_detail')
    
    


class CheckoutView(LoginRequiredMixin, CartMixin, TemplateView):
    """ create order view """
    template_name = 'dashboard/checkout.html'

    def post(self, request, *args, **kwargs):
        cart = self.get_cart()
        order = Order.objects.create(user=request.user, price=cart.total())
        for item in cart:
            product_type = item['type']
            product_id = item['product_id']
            if product_type == 'product':
                product = get_object_or_404(Product, id=product_id)
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    course=None,
                    product_type=product_type,
                    price=item['price'],
                )
            elif product_type == 'course':
                course = get_object_or_404(Course, id=product_id)
                OrderItem.objects.create(
                    order=order,
                    product=None,
                    course=course,
                    product_type=product_type,
                    price=item['price'],
                )
            else:
                continue
            
        cart.clear()
        return redirect('product:order_detail', order_id=order.id)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'ادامه فرایند خرید'
        return context
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
            "Amount": float(order.price), # total price >> it can cuase error cause its type 
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

def apply(request):
    if request.method == "POST":
        user = request.user
        user.is_mentor = True
        user.save()
        print("="*20,"\n",request.user.is_mentor)
        return HttpResponse("done")
    return HttpResponse("fucked")
    