from django.shortcuts import render

def index(request):
    return render(request, 'search/index.html')

def detail(request):
    search = request.POST['search']
    return render(request, 'search/detail.html', {'search':search})