from django.shortcuts import render

from .models import Category, Product

def index(request):
    products_list = Product.objects.all()
    print(products_list)
    context = {
        'products': products_list,
    }
    return render(request, 'index.html', context)

