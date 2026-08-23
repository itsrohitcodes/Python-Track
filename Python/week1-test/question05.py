# ----------------------------------------
# Function to calculate salary
# ----------------------------------------

def calculate_salary(basic_salary, bonus_percentage=5):

    # Calculate the bonus amount
    # Example:
    # If salary is 20,000 and bonus is 5%:
    # 20,000 * 5 / 100 = 1,000
    bonus_amount = basic_salary * bonus_percentage / 100

    # Add the bonus to the basic salary
    final_salary = basic_salary + bonus_amount

    # Return both calculated values
    return bonus_amount, final_salary


# ----------------------------------------
# Get employee information
# ----------------------------------------

# Ask for the employee's name
employee_name = input("Enter employee name: ")

# Ask for the employee's basic salary
basic_salary = int(input("Enter basic salary: "))


# ----------------------------------------
# Check for special bonus
# ----------------------------------------

# Ask whether the employee has a special bonus
special_bonus = input("Does the employee have a special bonus? ")


# Remove extra spaces and convert the answer
# to lowercase so that "YES", "Yes", and "yes"
# can all be treated the same
special_bonus = special_bonus.strip().lower()


# Check if the employee has a special bonus
if special_bonus == "yes":

    # Ask the user for the special bonus percentage
    bonus_percentage = int(input("Enter bonus percentage: "))

    # Send the salary and special bonus percentage
    # to the function
    bonus_amount, final_salary = calculate_salary(
        basic_salary,
        bonus_percentage
    )

else:

    # No special bonus was given.
    # The function will automatically use
    # its default bonus percentage of 5%.
    bonus_percentage = 5

    bonus_amount, final_salary = calculate_salary(
        basic_salary
    )


# ----------------------------------------
# Display salary information
# ----------------------------------------

print("\n----- Employee Salary -----")

print("Employee Name:", employee_name)

print("Basic Salary:", basic_salary)

print("Bonus Percentage:", bonus_percentage)

print("Bonus Amount:", bonus_amount)

print("Final Salary:", final_salary)
