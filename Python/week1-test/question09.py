# ----------------------------------------
# Create a Product class
# ----------------------------------------

class Product:

    # ----------------------------------------
    # Constructor
    # ----------------------------------------
    #
    # This method runs automatically when
    # we create a new Product object.
    #
    # It receives:
    # - product name
    # - price
    # - quantity

    def __init__(self, product_name, price, quantity):

        # Store the product name inside the object
        self.product_name = product_name

        # Store the product price inside the object
        self.price = price

        # Store the quantity inside the object
        self.quantity = quantity


    # ----------------------------------------
    # Calculate total price
    # ----------------------------------------

    def calculate_total(self):

        # Total price = price of one item
        # multiplied by the quantity
        total = self.price * self.quantity

        # Return the calculated total
        return total


    # ----------------------------------------
    # Check if this is a bulk order
    # ----------------------------------------

    def is_bulk_order(self):

        # If the customer ordered 10 or more
        # products, consider it a bulk order
        if self.quantity >= 10:
            return True

        # Otherwise, it is not a bulk order
        return False


    # ----------------------------------------
    # Find the order type
    # ----------------------------------------

    def get_order_type(self):

        # Call the is_bulk_order() method
        # to check the quantity
        if self.is_bulk_order():

            # Quantity is 10 or more
            return "Bulk Order"

        # Quantity is less than 10
        return "Regular Order"


    # ----------------------------------------
    # Display product information
    # ----------------------------------------

    def __str__(self):

        # This method controls what we see
        # when we print the Product object
        return f"Product Name: {self.product_name}"


# ----------------------------------------
# Get product information from the user
# ----------------------------------------

# Ask the user for the product name
product_name = input("Enter product name: ")

# Ask the user for the price
# int() converts the input into a whole number
price = int(input("Enter price: "))

# Ask the user for the quantity
quantity = int(input("Enter quantity: "))


# ----------------------------------------
# Create a Product object
# ----------------------------------------

# Create a Product object using the
# information entered by the user
product = Product(
    product_name,
    price,
    quantity
)


# ----------------------------------------
# Display product details
# ----------------------------------------

print("\n----- Product Details -----")

# Python automatically calls the __str__()
# method when we print the object
print(product)

# Display the price
print(f"Price: ₹{product.price}")

# Display the quantity
print(f"Quantity: {product.quantity}")

# Calculate and display the total amount
print(f"Total Amount: ₹{product.calculate_total()}")

# Find and display the order type
print(f"Order Type: {product.get_order_type()}")
