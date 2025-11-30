from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import Category, Product, Client, Order, OrderDetail
from .cart import Cart

from .forms import ClientForm
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
    if request.method == 'POST':
        quantity = int(request.POST['quantity'])
    else:
        quantity = 1

    objectProduct = Product.objects.get(pk=product_id)
    cart = Cart(request)
    cart.add(objectProduct, quantity)
    print(request.session.get('cart'))

    if request.method == 'GET':
        return redirect('/')
    
    return render(request, 'carrito.html')

def remove_from_cart(request, product_id):
    objectProduct = Product.objects.get(pk=product_id)
    cartProduct = Cart(request)
    cartProduct.remove(objectProduct)
    
    return render(request, 'carrito.html')

def clear_cart(request):
    cartProduct = Cart(request)
    cartProduct.clear()
    return render(request, 'carrito.html')


# View to create a user
def createUser(request):
    if request.method == 'POST':
        dataUser = request.POST['newUser']
        dataPassword = request.POST['newPassword']
        newUser = User.object.create_user(username=dataUser, email=dataUser, password=dataPassword)
        if newUser is not None:
            login(request, newUser)
            return redirect('/account')
            

    return render(request, 'login.html')


def accountUser(request):
    formClient = ClientForm()
    context = {
        'formClient': formClient
    }
    return render(request, 'cuenta.html')

def updateClient(request):
    message = ''
    if request.method == 'POST':
        formClient = ClientForm(request.POST)
        if formClient.is_valid():
            dataClient = formClient.cleaned_data
            # Update User
            updateUser = User.objects.get(pk=request.user.id)
            updateUser.first_name = dataClient['name']
            updateUser.last_name = dataClient['last_name']
            updateUser.email = dataClient['email']
            updateUser.save()

            # Register Client
            newClient = Client()
            newClient.user = updateUser
            newClient.dni = dataClient['dni']
            newClient.address = dataClient['address']
            newClient.phone = dataClient['phone']
            newClient.sex = dataClient['sex']
            newClient.birth_date = dataClient['birth_date']

            message = 'Client updated successfully'
        context = {
            'formClient': formClient,
            'message': message
        }



    return render(request, 'cuenta.html', context)