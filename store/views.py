from itertools import product
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from store.forms import ProductForm
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

# def create_view(request):
#     context ={}
 
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
         
#     context['form']= form
#     return render(request, "store/index.html", context)

def create_view(request):
    if request.method == "POST":
        product = Product.objects.create(
            title=request.POST['title'],
            slug=request.POST['slug'],
            desc=request.POST['desc'],
            image='products/' + request.POST['image'],
            price=request.POST['price'],
            quantity=request.POST['quantity'],
        )
        product.save()

    print("Le produit: ", product)
    return redirect('index')

def purchase(request, slug):
    product = get_object_or_404(Product, slug=slug)

    if request.method == 'POST':
        product.quantity -= 1

    return render(request, 'store/purchase.html', context={"product": product})