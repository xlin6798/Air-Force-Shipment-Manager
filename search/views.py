from django.shortcuts import render
from .models import Product

def index(request):
    product_list = Product.objects.order_by('-product_un')[:5]
    context = {'product_list': product_list}
    return render(request, 'search/index.html', context)