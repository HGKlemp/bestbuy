class Product:


    def __init__(self, name, price, quantity, active=True):

        if not isinstance(name, str) or not name:
            raise ValueError("Name must be a non-empty string.")

        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be a non-negative float.")

        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")

        if not isinstance(active, bool):
            raise ValueError("Active must be a boolean.")

        self.active = active
        self.quantity = quantity
        self.name = name
        self.price = price

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity

    def is_active(self):
        return self.active

    def active(self):
        self.active = True

    def deactive(self):
        self.active = False

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity):
        if self.quantity - quantity < 0:
            raise ValueError("Purchase quantity is greater than the available quantity.")

        self.quantity -= quantity

        return quantity * self.price

bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = Product("MacBook Air M2", price=1450, quantity=100)

print(bose.buy(50))
print(mac.buy(100))
print(mac.is_active())

bose.show()
mac.show()

bose.set_quantity(1000)
bose.show()
