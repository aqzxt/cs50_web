class Cart:
    '''Save user orders in a dictionary'''

    def __init__(self):
        self.cart = {}

    def add_order(self, pk, order):
        '''Map pk key to order value'''
        self.cart[pk] = order

    def remove_order(self, pk):
        '''Delete order'''
        del self.cart[pk]

    def get_cart(self):
        return self.cart

    def get_order(self, pk):
        return self.cart.get(pk)
