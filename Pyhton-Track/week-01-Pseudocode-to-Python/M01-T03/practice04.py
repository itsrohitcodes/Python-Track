# Track changes across aliased and copied lists

# Process list operations and comparisons
value_count = int(input())
original_list = []

# Read and store all values using append()
for i in range(value_count):
    lst = int(input())
    original_list.append(lst)

# Create an alias and a shallow copy
alias_list = original_list
copied_list = original_list.copy()

# Get input for updates
alias_position = int(input())
alias_value = int(input())
copy_position = int(input())
copy_value = int(input())

# Update one value through the alias
alias_list[alias_position - 1] = alias_value

# Update one value in the copied list
copied_list[copy_position - 1] = copy_value

# Compare both lists position by position
for i in range(len (original_list)):
    if original_list[i] == alias_list[i]:
        condition = "Yes"
    else:
        condition = "No"

# set different positions counter
different_positions = 0
for i in range(len (original_list)):
    if original_list[i] != copied_list[i]:
        different_positions += 1

# Display all results
print(f"Original List: {original_list}")
print(f"Alias List: {alias_list}")
print(f"Copied List: {copied_list}")
print(f"Alias Shares Original: {condition}")
print(f"Different Positions: {different_positions}")