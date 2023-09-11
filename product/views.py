from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Count 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from taggit.models import Tag 
from .models import Product
from .cart_module import Cart
from home.models import ShareLinks
from django.contrib.auth.decorators import login_required


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
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("product:cart_detail")


@login_required
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("product:cart_detail")


@login_required
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("product:cart_detail")


@login_required
def cart_detail(request):
    context = {}
    if request.method == 'POST':
        items = request.POST.get('id')
        context['items']=items
    return render(request, 'dashboard/cart_detail.html', context)

# ===================================  =================================== 
