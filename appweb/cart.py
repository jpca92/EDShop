class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session

        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        
        self.cart = cart
    
    def add(self, product, quantity=1):
        self.cart[product.id] = {
            'product_id':product.id,
            'name': product.name,
            'quantity': quantity,
            'price': str(product.price),
            'image': product.image.url,
            'category': product.category.name,
            'category_id': product.category.id,
            'subtotal': str(quantity * product.price)
        }
        print(f"adding {self.cart[product.id]} to cart")
        self.save()

    def remove(self, product):
        pass

    def clear(self):
        pass

    def save(self):
        self.session['cart'] = self.cart
        self.session.modified = True
