from  .order import Order 

class Customer:
    def __init__(self, name):
        if type(name) == str and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")
        self._orders = []

    @property
    def name(self):
        return self._name

    def orders(self):
        return self._orders

    def coffees(self):
        return list(set(order.coffee for order in self._orders))

    def create_order(self, coffee, price):
        new_order = Order(self, coffee, price)
        self._orders.append(new_order)
        return new_order

    @classmethod
    def most_aficionado(cls, coffee):
        customers = coffee.customers()
        if not customers:
            return None

        highest_spender = None
        max_spent = 0

        for customer in customers:
            total_spent = 0
            for order in customer.orders():
                if order.coffee == coffee:
                    total_spent += order.price
            
            if total_spent > max_spent:
                max_spent = total_spent
                highest_spender = customer
        
        return highest_spender
