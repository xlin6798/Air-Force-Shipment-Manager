from queue import Empty
from django.shortcuts import render
from .models import HazSubstance, Product, SpCode, HazClass
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import re

def index(request):
    products = Product.objects.order_by('un').all()
    context = {'products': products}
    return render(request, 'search/index.html', context)

def detail(request, pid):
    product = Product.objects.get(id=pid)

    hazcode = product.hazard
    haz_class = ""
    if hazcode != "":
        hazcode = re.sub(r'[^0-9.]', '', hazcode)
        #print(hazcode)
        haz_class = HazClass.objects.get(code=hazcode)

    subcodes = product.sub_as_list()
    sub_list = []
    if subcodes:
        for subcode in subcodes:
            subcode = re.sub(r'[^0-9.]', '', subcode)
            sub = HazClass.objects.get(code=subcode)
            sub_list.append(sub)

    spcodes = product.sp_as_list()
    sp_list = []
    if spcodes:
        for spcode in spcodes:
            code = SpCode.objects.get(code=spcode.strip())
            sp_list.append(code)

    ppcode = product.paragraph
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

def hazard(request):
    hazsubstances = HazSubstance.objects.order_by('psn').all()
    context = {'hazsubstances': hazsubstances}
    return render(request, 'search/hazard.html', context)

def shipmentHistory(request):
    return render(request, 'search/shipmentHistory.html')

def source(request):
    return render(request, 'search/source.html')

def conversion(request):
    return render(request, 'search/conversion.html')