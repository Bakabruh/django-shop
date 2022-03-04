from itertools import product
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Product

def index(request):
    products = Product.objects.all()

    return render(request, 'store/index.html', context={"products": products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)

    return render(request, 'store/detail.html', context={"product": product})

def delete_product(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == 'POST':
        product.delete()
        return redirect('index')

    return render(request, 'store/delete.html', context={"product": product})