from django.shortcuts import render
from .models import Product

def index(request):
    product_list = Product.objects.order_by('product_un').all()
    context = {'product_list': product_list}
    return render(request, 'search/index.html', context)

def detail(request):
    search = request.POST['search']
    product_list = Product.objects.filter(product_un__icontains=search)
    return render(request, 'search/detail.html', {'product_list':product_list})

def shipmentHistory(request):
    return render(request, 'search/shipmentHistory.html')
