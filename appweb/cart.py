class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session

        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        
        self.cart = cart
    
    def add(self, product, quantity=1):
        pass
    def remove(self, product):
        pass
    def clear(self):
        pass
    def save(self):
        pass