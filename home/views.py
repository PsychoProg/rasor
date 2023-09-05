from django.shortcuts import render
from .models import ListBox, News, PageContent1, PageContent2, ShareLinks
from product.models import Product
from core.decorators import mentor_required


def home_view(request):
    list_items = ListBox.published.all()
    products = Product.published.all()
    news = News.published.all()
    page_content_1 = PageContent1.objects.last()
    page_content_2 = PageContent2.objects.last()
    context = {
        'title': 'صفحه اصلی',
        'list_items': list_items,
        'products': products,
        'news': news,
        'page_content_1': page_content_1,
        'page_content_2': page_content_2,
    }
    return render(request, 'home/home.html', context)

