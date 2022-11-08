from django.shortcuts import render
from .models import Product, SpCode, HazClass

def index(request):
    product_list = Product.objects.order_by('product_un').all()
    context = {'product_list': product_list}
    return render(request, 'search/index.html', context)

def detail(request, un_code):
    product_list = Product.objects.filter(product_un__icontains=un_code)
    code_list = []
    for code in product_list[0].product_haz_class.split(','):
        code_list.append(SpCode.objects.filter(sp_code__icontains=code))
    return render(request, 'search/detail.html', {'product_list':product_list, 'code_list':code_list})

def shipmentHistory(request):
    return render(request, 'search/shipmentHistory.html')
