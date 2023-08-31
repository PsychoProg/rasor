from django.shortcuts import render
from .models import ListBox, News
from blog.models import Product
from core.decorators import mentor_required


def home_view(request):
    list_items = ListBox.published.all()
    products = Product.published.all()
    news = News.published.all()
    context = {
        'list_items': list_items,
        'products': products,
        'news': news,
    }
    return render(request, 'home/home.html', context)
