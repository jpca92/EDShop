from django.urls import path

from . import views

app_name = 'appweb'

urlpatterns = [
    path('', views.index, name='index'),
    path('productsPerCategory/<int:category_id>', views.productsPerCategory, name='productsPerCategory'),
    path('productsPerName', views.productsPerName, name='productsPerName'),
    path('product/<int:product_id>', views.productDetail, name='productDetail'),
    path('cart', views.shopping_cart, name='shopping_cart'),
    path('addtocart/<int:product_id>', views.add_to_cart, name='addtocart'),
    path('removefromcart/<int:product_id>', views.remove_from_cart, name='removefromcart'),
    path('clearcart', views.clear_cart, name='clearcart'),
    
       
]