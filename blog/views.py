from django.shortcuts import get_object_or_404, render
from django.views.generic import DeleteView, ListView 


def testview(request):
    return render(request, 'product/products_list.html', {})