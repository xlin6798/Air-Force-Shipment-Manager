from queue import Empty
from django.shortcuts import render
from .models import Product, SpCode, HazClass
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import re

def index(request):
    products = Product.objects.order_by('product_un').all()
    context = {'products': products}
    return render(request, 'search/index.html', context)

def detail(request, un_code):
    product = Product.objects.get(product_un=un_code)

    hazcode = product.product_haz_class
    haz_class = ""
    if hazcode != "":
        hazcode = re.sub(r'[^0-9.]', '', hazcode)
        #print(hazcode)
        haz_class = HazClass.objects.get(haz_num=hazcode)

    subnums = product.sub_as_list()
    sub_list = []
    if subnums:
        for subnum in subnums:
            subnum = re.sub(r'[^0-9.]', '', subnum)
            sub = HazClass.objects.get(haz_num=subnum)
            sub_list.append(sub)

    spcodes = product.sp_as_list()
    sp_list = []
    if spcodes:
        for spcode in spcodes:
            code = SpCode.objects.get(sp_code=spcode.strip())
            sp_list.append(code)

    ppcode = product.product_paragraph
    pp = ppcode
    if ppcode != "" and ppcode != "FORBIDDEN":
        pp = ""
        for c in ppcode:
            if c != '.':
                pp += c
            else:
                break

    context = {'product':product, 'haz_class':haz_class, 'sub_list':sub_list, 'sp_list':sp_list, 'pp':pp}
    return render(request, 'search/detail.html', context)

def shipmentHistory(request):
    return render(request, 'search/shipmentHistory.html')

def source(request):
    return render(request, 'search/source.html')