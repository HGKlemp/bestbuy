class Product:
    """Represents a product in the store."""

    def __init__(self, name, price, quantity, active=True):
        """Creates a new product."""
        if not isinstance(name, str) or not name:
            raise ValueError("Name must be a non-empty string.")

        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be a non-negative number.")

        if type(quantity) is not int or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")

        if not isinstance(active, bool):
            raise ValueError("Active must be a boolean.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = active

    def get_quantity(self):
        """Returns the available quantity."""
        return self.quantity

    def set_quantity(self, quantity):
        """Updates the available quantity."""
        if type(quantity) is not int or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")

        self.quantity = quantity

        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        """Returns whether the product is active."""
        return self.active

    def activate(self):
        """Activates the product."""
        self.active = True

    def deactivate(self):
        """Deactivates the product."""
        self.active = False

    def show(self):
        """Displays the product information."""
        print(
            f"{self.name}, Price: {self.price}, "
            f"Quantity: {self.quantity}"
        )

    def buy(self, quantity):
        """Buys a quantity and returns its price."""
        if type(quantity) is not int or quantity <= 0:
            raise ValueError("Purchase quantity must be a positive integer.")

        if quantity > self.quantity:
            raise ValueError(
                "Purchase quantity is greater than the available quantity."
            )

        self.quantity -= quantity

        if self.quantity == 0:
            self.deactivate()

        return quantity * self.price


