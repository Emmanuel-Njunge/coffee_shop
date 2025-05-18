from lib.customer import Customer
from lib.coffee import Coffee
from lib.order import Order


customer1 = Customer("Emmanuel")
coffee1 = Coffee("Latte")

order1 = customer1.create_order(coffee1, 5.0)
print(order1.customer.name)  # Prints "Emmanuel"
print(order1.coffee.name)    # Prints "Latte"
