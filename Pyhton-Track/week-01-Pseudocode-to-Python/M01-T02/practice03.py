# Calculate the sum of digits

number = int(input())
sum_of_digits = 0

# Extract and add each digit using a while loop
while number != 0:
    last_digits = number % 10
    sum_of_digits = sum_of_digits + last_digits
    number = number // 10

print(f"Sum of Digits: {sum_of_digits}")