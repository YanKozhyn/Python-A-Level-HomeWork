class Product:
    def __init__(self, name, price, quantity) -> None:
        self.name = name
        self.price = price
        self.__quantity = quantity
    def calculate_price(self):
        return f"Total price: {self.price * self.__quantity}"

class ShoppingCart(Product):
    def __init__(self,name, price, quantity):
        super().__init__(name, price,quantity)
        super().calculate_price()
        
cart1 = ShoppingCart("banana", 5, 2)

print(cart1.calculate_price())
    