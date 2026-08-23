# ----------------------------------------
# Function to calculate the shopping bill
# ----------------------------------------

def calculate_bill(unit_price, quantity):

    # Multiply the price of one item
    # by the number of items purchased
    total_amount = unit_price * quantity


    # ----------------------------------------
    # Calculate discount
    # ----------------------------------------

    # If the total amount is ₹2000 or more,
    # give the customer a 10% discount
    if total_amount >= 2000:

        # Calculate 10% of the total amount
        discount = total_amount * 0.10

    # If the total is less than ₹2000,
    # there is no discount
    else:
        discount = 0


    # ----------------------------------------
    # Calculate final amount
    # ----------------------------------------

    # Subtract the discount from the total amount
    final_amount = total_amount - discount


    # Return all three calculated values
    return total_amount, discount, final_amount


# ----------------------------------------
# Get product information from the user
# ----------------------------------------

# Ask for the product name
product_name = input("Enter product name: ")

# Ask for the price of one product
# float() allows decimal prices such as 99.50
unit_price = float(input("Enter price: "))

# Ask how many products the customer wants
# int() is used because quantity should be a whole number
quantity = int(input("Enter quantity: "))


# ----------------------------------------
# Calculate the bill
# ----------------------------------------

# Send the price and quantity to our function
# The function gives back three values
total_amount, discount, final_amount = calculate_bill(
    unit_price,
    quantity
)


# ----------------------------------------
# Display the shopping bill
# ----------------------------------------

print("\n----- Shopping Bill -----")

print("Product Name:", product_name)

print(f"Price: ₹{unit_price:.2f}")

print("Quantity:", quantity)

print(f"Total Amount: ₹{total_amount:.2f}")

print(f"Discount: ₹{discount:.2f}")

print(f"Final Amount: ₹{final_amount:.2f}")
