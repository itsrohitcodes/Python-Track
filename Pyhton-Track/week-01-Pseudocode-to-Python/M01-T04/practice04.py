# Calculate and return total marks using a function

# Create and call calculate_total() function
def calculate_total(first_mark, second_mark):
    # Calculate and return the total marks
    total = first_mark + second_mark
    return total

# Read inputs and call function
mark1 = int(input())
mark2 = int(input())

# Call the function and store the returned value 
total = calculate_total(mark1, mark2)

# Print the returned value
print(total)