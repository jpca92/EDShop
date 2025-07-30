class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session

        cart = self.session.get('cart')
        total_amount = self.session.get('cartTotalAmount')

        if not cart:
            cart = self.session['cart'] = {}
            total_amount = self.session['cartTotalAmount'] = '0'
        
        self.cart = cart
        self.total_amount = float(total_amount)
    
    def add(self, product, quantity=1):
        if str(product.id) not in self.cart:
            self.cart[str(product.id)] = {
                'product_id':product.id,
                'name': product.name,
                'quantity': quantity,
                'price': str(product.price),
                'image': product.image.url,
                'category': product.category.name,
                'category_id': product.category.id, # category id for future use
                'subtotal': str(quantity * product.price)
            }
        else:
            # if the product is already in the cart, update the quantity
            for key, value in self.cart.items():
                if key == str(product.id):
                    value['quantity'] = str(int(value['quantity']) + quantity)
                    value['subtotal'] = str(int(value['quantity']) * float(value['price']))
                    break

        print(f"adding {self.cart[str(product.id)]} to cart")
        self.save()

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        self.session['cart'] = {}
        self.session['cartTotalAmount'] = '0'

    def save(self):

        total_amount = 0
        for key, value in self.cart.items():
            total_amount += float(value['subtotal'])

        self.session['cartTotalAmount'] = total_amount
        self.session['cart'] = self.cart
        self.session.modified = True

