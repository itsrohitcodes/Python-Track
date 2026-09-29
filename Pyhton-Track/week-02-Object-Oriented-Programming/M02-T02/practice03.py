# Create a Product using an Alternative Constructor

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def from_string(cls, data):
        # Create and return the Product object
        name, price = data.split(",")
        name = name.strip()
        price = price.strip()

        return cls(name, price)


data = input().strip()
product = Product.from_string(data)

print(f"Product: {product.name}")
print(f"Price: {product.price}")