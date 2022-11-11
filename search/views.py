from queue import Empty
from django.shortcuts import render
from .models import Product, SpCode, HazClass

def index(request):
    product_list = Product.objects.order_by('product_un').all()
    context = {'product_list': product_list}
    return render(request, 'search/index.html', context)

def detail(request, un_code):
    product = Product.objects.filter(product_un__icontains=un_code)[0]
    hazcode = product.product_haz_class
    haz_list = []
    if hazcode != "":
        haz_list = HazClass.objects.filter(haz_num__icontains=hazcode)
    spcodes = product.sp_as_list()
    sp_list = []
    if spcodes:
        for spcode in spcodes:
            code = SpCode.objects.filter(sp_code__icontains=spcode.strip())[0]
            sp_list.append(code)
    
    return render(request, 'search/detail.html', {'product':product, 'haz_list':haz_list, 'sp_list':sp_list})

def shipmentHistory(request):
    return render(request, 'search/shipmentHistory.html')

def source(request):
    return render(request, 'search/source.html')