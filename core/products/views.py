# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Product

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'products/product_detail.html', {'product': product})

def all_products(request):
    products = Product.objects.all()  # Retrieve all products
    return render(request, 'products/all_products.html', {'products': products})