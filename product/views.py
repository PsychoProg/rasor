from django.shortcuts import get_object_or_404, render
from django.db.models import Count 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from taggit.models import Tag 
from .models import Product


def product_list(request, tag_slug=None):
    products = Product.objects.all()
    tags = Tag.objects.all()
    if tag_slug:
        tags = get_object_or_404(Tag, slug=tag_slug)
        products = Product.published.filter(tags__in=[tags])

    context = {
        'title': 'لیست محصولات',
        'products': products,
        'tags': tags,
    }
    return render(request, 'home/list.html', context)


def product_detail(request, pk, slug):
    product = get_object_or_404(Product, id=pk, slug=slug)
    tags = product.tags.values_list('id', flat=True)
    similar_products = Product.published.filter(tags__in=tags).exclude(id=pk, slug=slug)
    similar_products = similar_products.annotate(tags_count=Count('tags')).order_by('-created_at')[:4]

    context = {
        'title': product.title,
        'items': product,
        'similar_items': similar_products,
    }
    return render(request, 'home/detail.html', context)