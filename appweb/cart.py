class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session

        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        
        self.cart = cart
    
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
        pass

    def clear(self):
        pass

    def save(self):
        self.session['cart'] = self.cart
        self.session.modified = True
