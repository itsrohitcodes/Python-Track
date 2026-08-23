# Ask the user to enter the customer's name
customer_name = input("Enter customer name: ")

# Ask the user to enter the number of units consumed
# float() allows the user to enter decimal values too
units = float(input("Enter units consumed: "))


# ----------------------------------------
# Calculate the electricity charge
# ----------------------------------------

# If the customer used 100 units or less
if units <= 100:
    electricity_charge = units * 2

# If the customer used more than 100
# but 200 units or less
elif units <= 200:

    # First 100 units cost ₹2 per unit
    first_100_units = 100 * 2

    # Units above 100 cost ₹3 per unit
    extra_units = units - 100
    extra_charge = extra_units * 3

    # Add both charges
    electricity_charge = first_100_units + extra_charge

# If the customer used more than 200 units
else:

    # First 100 units cost ₹2 per unit
    first_100_units = 100 * 2

    # Next 100 units cost ₹3 per unit
    next_100_units = 100 * 3

    # Units above 200 cost ₹5 per unit
    extra_units = units - 200
    extra_charge = extra_units * 5

    # Add all three charges
    electricity_charge = (
        first_100_units
        + next_100_units
        + extra_charge
    )


# ----------------------------------------
# Calculate the surcharge
# ----------------------------------------

# If the electricity charge is more than ₹1000,
# add a 5% surcharge
if electricity_charge > 1000:
    surcharge = electricity_charge * 0.05

# Otherwise, there is no surcharge
else:
    surcharge = 0


# ----------------------------------------
# Calculate the final bill
# ----------------------------------------

# Final bill = electricity charge + surcharge
final_bill = electricity_charge + surcharge


# ----------------------------------------
# Display the bill
# ----------------------------------------

print("\n----- Electricity Bill -----")

print(f"Customer Name: {customer_name}")
print(f"Units Consumed: {units:g}")
print(f"Electricity Charge: ₹{electricity_charge:.2f}")
print(f"Surcharge: ₹{surcharge:.2f}")
print(f"Final Bill: ₹{final_bill:.2f}")
