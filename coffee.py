from order import Order

class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) >= 3:
            self._name = value
        else:
            raise ValueError("Name must be a string with at least 3 characters.")

    def num_orders(self):
        return len([order for order in Order.all if order.coffee == self])

    def average_price(self):
        prices = [order.price for order in Order.all if order.coffee == self]
        return sum(prices) / len(prices) if prices else 0