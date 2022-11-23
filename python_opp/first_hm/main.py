class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def total_price(self, quantity):
        return

    
class ShoppingCart:
    def __init__(self, product: Product, quantity):
        self.products = product
        self.quantity = quantity

    def add_product(self, product: Product, quantity):
        ...
        
    def total_price(self):
        return f"Your total price: {self.products.price * self.quantity}"

    
bear = Product("Bear", 5.5)  # те, що ти хочеш - beer, а медведя на 5.5 я би також придбав
print(bear.price_of_product())
chips = Product("Chips", 10)
cart = ShoppingCart(bear, 2)
print(cart.total_price())


if __name__ == "__main__":
    apple = Product("apple", 15.1)
    assert apple.total_price(0.7) == 10.57
    cart = ShoppingCart()
    cart.add_product(apple, 0.7)
    cart.add_product(Product("beer", 42), 1)
    assert cart.total_price() == 52.57
