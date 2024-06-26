from django.shortcuts import get_object_or_404, render
from product.models import Product
from .models import ListBox, News, PageContent1, PageContent2, ShareLinks, AboutUs
from dashboard.models import Course 


# =================================== Home View =================================== 
def home_view(request):
    list_items = ListBox.published.all()
    products = Product.published.all()[:3]
    news = News.published.all()[:4]
    page_content_1 = PageContent1.objects.last()
    page_content_2 = PageContent2.objects.last()
    links = ShareLinks.objects.all()
    context = {
        'title': 'صفحه اصلی',
        'list_items': list_items,
        'products': products,
        'news': news,
        'page_content_1': page_content_1,
        'page_content_2': page_content_2,
        'links': links,
    }
    return render(request, 'home/home.html', context)

# =================================== News Views =================================== 
def news_detail(request, pk, slug):
    news = get_object_or_404(News, id=pk, slug=slug)
    tags = news.tags.values_list('id', flat=True)
    links = ShareLinks.objects.all()
    context = {
        'title': news.title,
        'links': links,
        'tags': tags,
        'items': news,
    }
    return render(request, 'home/detail.html', context)


def news_list(request):
    news = News.published.all()
    links = ShareLinks.objects.all()
    context = {
        'items': news,
        'links': links,
    }
    return render(request, 'home/list.html', context)

# =================================== About Us =================================== 
def about_view(request):
    about = AboutUs.objects.last()
    links = ShareLinks.objects.all()
    context = {
        'items': about,
        'links': links,
    }
    return render(request, 'home/about_us.html', context)

# =================================== About Us ===================================
def course_list(request, course_type):
    # academics = Course.objects.filter(type='academics')
    print('*'*20,'\n',course_type)
    academics = Course.objects.filter(type=course_type)
    
    links = ShareLinks.objects.all()
    context = {
        'items': academics,
        'links': links,
        'course': True, 
        'course_type': course_type,
    }
    return render(request, 'home/list.html', context)