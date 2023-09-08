from django.shortcuts import get_object_or_404, render
from product.models import Product
from .models import ListBox, News, PageContent1, PageContent2


def home_view(request):
    list_items = ListBox.published.all()
    products = Product.published.all()[:3]
    news = News.published.all()[:4]
    page_content_1 = PageContent1.objects.last()
    page_content_2 = PageContent2.objects.last()
    context = {
        'title': 'صفحه اصلی',
        'list_items': list_items,
        'products': products,
        'news': news,
        'page_content_1': page_content_1,
        'page_content_2': page_content_2,
        'contact_alert': False
    }
    return render(request, 'home/home.html', context)


def news_detail(request, pk, slug):
    news = get_object_or_404(News, id=pk, slug=slug)
    tags = news.tags.values_list('id', flat=True)

    context = {
        'title': news.title,
        'tags': tags,
        'items': news,
    }
    return render(request, 'home/detail.html', context)


