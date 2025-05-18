from .order import Order  # Impot orders so that coffee can use it

class Coffee:
    def __init__(self, name):
        if type(name) == str and len(name) >= 3:
            self._name = name
        else:
            raise ValueError("Coffee name must be at least 3 characters long.")
        self._orders = []

    @property
    def name(self):
        return self._name

    def orders(self):
        return self._orders

    def customers(self):
        return list(set(order.customer for order in self._orders))

    def num_orders(self):
        return len(self._orders)

    def average_price(self):
        if not self._orders:
            return 0

        total_price = 0
        for order in self._orders:
            total_price += order.price
        
        return total_price / len(self._orders)
