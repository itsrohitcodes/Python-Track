# Process a fixed product record

# Read the product details from the user
product_id = input()
product_name = input()
category = input()
unit_price = float(input())
quantity = int(input())
reorder_level = int(input())

# Create the fixed product record as a tuple
tuple= (product_id, product_name, category, unit_price, quantity)

# Access the product ID and product name using indexes
(product_id[0])
(product_name [1])

# Unpack the complete tuple
p_id, name, p_category, price, p_quantity = tuple

# Calculate the stock value
stock_value = unit_price * quantity

# Determine the stock status
if quantity == 0:
    stock_status = "Out of Stock"
elif quantity <= reorder_level:
    stock_status = "Reorder Required"
else:
    stock_status = "Sufficient Stock"

# Display the processed product record
print(f"Product ID: {p_id}")
print(f"Product Name: {name}")
print(f"Category: {p_category}")
print(f"Unit Price: {price:.2f}")
print(f"Available Quantity: {p_quantity}")
print(f"Stock Value: {stock_value:.2f}")
print(f"Stock Status: {stock_status}")