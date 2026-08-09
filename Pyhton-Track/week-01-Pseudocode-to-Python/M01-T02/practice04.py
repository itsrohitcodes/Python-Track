# Count numbers divisible by 3

# take input from user
starting_number = int(input())
ending_number = int(input())

# initialize the counter
count = 0

# Visit every number and count the values divisible by 3
for i in range (starting_number, ending_number + 1): 
    if i % 3 == 0:
        count = count + 1
# print the result
print(f"Divisible by 3: {count}")