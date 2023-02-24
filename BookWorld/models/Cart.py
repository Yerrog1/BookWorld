class Cart:

    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get("carrito")
        if not cart:
            self.session["cart"] = {}
            self.cart = self.session["cart"]
        else:
            self.cart = cart

    def add(self, product):
        isbn = str(product.isbn)
        if isbn not in self.cart.keys():
            self.cart[isbn] = {
                'product_isbn': product.isbn,
                'name': product.title,
                'acumulated': product.price,
                'quantity': 1,
            }
        else:
            self.cart[isbn]['quantity'] += 1
            self.carrito[isbn]['price'] = product.price
        self.saveCart()

    def saveCart(self):
        self.session['cart'] = self.cart
        self.session.modified = True

    def remove(self, product):
        isbn = str(product.isbn)
        if isbn in self.cart:
            del self.cart[isbn]
            self.saveCart()

    def subtract(self, product):
        isbn = str(product.isbn)
        if isbn in self.cart.keys():
            self.cart[isbn]['quantity'] -= 1
            self.cart[isbn]['price'] -= product.price
            if self.cart[isbn]['quantity'] < 1:
                self.remove(product)
            self.saveCart()

    def clear(self):
        self.session['cart'] = {}
        self.session.modified = True
