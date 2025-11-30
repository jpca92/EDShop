import datetime
from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    registry_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    registry_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='products', blank=True, null=True)
    stock = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.RESTRICT)
    dni = models.CharField(max_length=20, unique=True)
    sex = models.CharField(max_length=10, null=True)
    phone = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.dni
    
class Order(models.Model):

    STATUS_CHOICES = (
        ('0', 'Pending'),
        ('1', 'Shipped'),
    )
    # Check this later.ForeignKey(
    client = models.ForeignKey(Client, on_delete=models.RESTRICT)
    registry_date = models.DateTimeField(auto_now_add=True)
    n_order = models.CharField(max_length=20, null=True)
    total_mount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='0')
    
    def __str__(self):
        return self.n_order
    
class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.RESTRICT)
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    quantity = models.IntegerField(default=1)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.product.name
    