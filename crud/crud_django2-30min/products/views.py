from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

def list_products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

'''def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_products')

    return render(request, 'products_form.html', {'form': form})'''

'''def update_product(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=product)'''

