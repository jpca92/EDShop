from django.shortcuts import render, redirect, get_object_or_404

from .models import Category, Product
from .cart import Cart

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

# This view is used to filter products by name using a form in the index.html - header.html template
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

def productDetail (request, product_id):
    # objProduct = Product.objects.get(pk=product_id)
    objProduct = get_object_or_404(Product, pk=product_id)
    context = {
        'product': objProduct,

    }
    return render (request, 'producto.html', context)

""" views for shopping cart """

def shopping_cart(request):
    return render (request, 'carrito.html')

def add_to_cart(request, product_id):
    quantity = 1

    objectProduct = Product.objects.get(pk=product_id)
    cart = Cart(request)
    cart.add(objectProduct, quantity)
    print(request.session.get('cart'))
    return render(request, 'carrito.html')