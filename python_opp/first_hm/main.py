class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def price_of_product(self):
        return f"Price: {self.price} of product: {self.name}"

class ShoppingCart:
    def __init__(self, product: Product, quantity):
        self.products = product
        self.quantity = quantity
    def total_price(self):
        return f"Your total price: {self.products.price * self.quantity}"

bear = Product("Bear", 5.5)
print(bear.price_of_product())
chips = Product("Chips", 10)
cart = ShoppingCart(bear, 2)
print(cart.total_price())
