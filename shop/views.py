from django.shortcuts import render ,get_object_or_404
from .models import Product , Category
from django.db.models import Q
from django.core.paginator import Paginator

import pprint
# Create your views here.

def index(request):
    if request.GET.get('item_name',None):
        param = request.GET.get('item_name')
        product = Product.objects.filter(Q(title__icontains=param)).select_related('category').all()
    else:
        product = Product.objects.select_related('category').all()

    #paginator code
    paginator = Paginator(product,3)
    page = request.GET.get('page')
    product = paginator.get_page(page)
    context = {
        'product': product
    }
    return render(request,'shops/index.html',context)

def detail(request,id):
    product = get_object_or_404(Product,pk=id)
    context = {
        'product': product
    }
    return render(request,'shops/detail.html',context)