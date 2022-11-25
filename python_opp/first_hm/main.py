class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def total_price(self, quantity):
        return round(self.price * quantity, 2)

class ShoppingCart:
    def __init__(self):
        self.order = {}
    def add_product(self, product: Product, quantity):
        self.order.update({product: quantity})
    def total_price(self):
        result = 0
        for (product,quantity) in self.order.items():
            result += product.total_price(quantity)
        return result
    def display_product(self):
        for (k, v) in self.order.items():
            print(f'Price of {k.name}: {k.price}, amount of your product: {v}')


if __name__ == "__main__":
    apple = Product("apple", 15.1)
    assert apple.total_price(0.7) == 10.57
    cart = ShoppingCart()
    cart.add_product(apple, 0.7)
    cart.add_product(Product("beer", 42), 1)
    assert cart.total_price() == 52.57
