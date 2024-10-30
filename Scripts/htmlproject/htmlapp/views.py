from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
import datetime

def home(request):
    # Fetch all products
    prod1 = Product.objects.all()
    return render(request, 'nextpage.html', {'prods': prod1, 'action': 'create'})

def create_task(request):
    all_products = Product.objects.all()

    if request.method == 'POST':
        # Create new product
        name = request.POST.get('pname')
        price = request.POST.get('price')
        description = request.POST.get('description')
        created_at = datetime.datetime.now()
        
        prod = Product(name=name, price=price, description=description, created_at=created_at)
        prod.save()
        return redirect('home')
    
    return render(request, 'nextpage.html', {'action': 'create', 'prods': all_products})

def update_product(request, pk):
    product = get_object_or_404(Product, id=pk)
    all_products = Product.objects.all()

    if request.method == 'POST':
        # Update product details
        product.name = request.POST.get('pname')
        product.price = request.POST.get('price')
        product.description = request.POST.get('description')
        product.save()
        return redirect('home')

    return render(request, 'nextpage.html', {'product': product, 'action': 'update','prods': all_products})

def delete_product(request, pk):
    product = get_object_or_404(Product, id=pk)
    all_products = Product.objects.all()
    
    if request.method == 'POST':
        product.delete()
        return redirect('home')

    return render(request, 'nextpage.html', {'product': product, 'action': 'delete', 'prods': all_products})
