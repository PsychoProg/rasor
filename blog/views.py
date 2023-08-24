from django.shortcuts import get_object_or_404, render
from django.views.generic import DeleteView, ListView 
from .models import Product
from taggit.models import Tag 


def product_list(request, tag_slug=None):
    products = Product.objects.all()
    tags = Tag.objects.all()
    if tag_slug:
        tags = get_object_or_404(Tag, slug=tag_slug)
        products = Product.objects.filter(tags__in=[tags])

    context = {
        'products': products,
        'tags': tags,
    }
    return render(request, 'dashboard/products_list.html', context)
