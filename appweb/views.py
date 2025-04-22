from django.shortcuts import render, redirect

from .models import Category, Product

def index(request):
    products_list = Product.objects.all()
    categories_list = Category.objects.all()

    # print(products_list)
    context = {
        'products': products_list,
        'categories': categories_list,
    }
    return render(request, 'index.html', context)

def productsPerCategory(request, category_id):
    objectCategory = Category.objects.get(pk=category_id)
    print(objectCategory)
    # products_list = Product.objects.filter(category=objectCategory)
    products_list = objectCategory.product_set.all()
    categories_list = Category.objects.all()

    context = {
        'products': products_list,
        'categories': categories_list,
        'objectCategory': objectCategory,
    }
    return render(request, 'index.html', context)


def productsPerName(request):
    name = ''
    if request.method == 'POST':
        name = request.POST.get('name', '')
        if not name:
            return redirect('appweb:index')  # vuelve al home si no se busca nada

    products_list = Product.objects.filter(name__icontains=name)
    categories_list = Category.objects.all()

    context = {
        'products': products_list,
        'categories': categories_list,
    }
    print(f"Buscando productos que contengan: {name}")

    return render(request, 'index.html', context)


