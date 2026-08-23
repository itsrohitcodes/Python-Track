# ----------------------------------------
# Function to analyze the numbers
# ----------------------------------------

def analyze_numbers(numbers):

    # Add all numbers together
    total = sum(numbers)

    # Calculate the average
    average = total / len(numbers)

    # Find the highest number
    highest = max(numbers)

    # Find the lowest number
    lowest = min(numbers)


    # ----------------------------------------
    # Count even and odd numbers
    # ----------------------------------------

    # Start both counters at zero
    even_count = 0
    odd_count = 0

    # Check every number in the list
    for num in numbers:

        # The % operator gives the remainder.
        # If the remainder is 0, the number is even.
        if num % 2 == 0:
            even_count += 1

        # Otherwise, the number is odd
        else:
            odd_count += 1


    # Return all the results
    return (
        total,
        average,
        highest,
        lowest,
        even_count,
        odd_count
    )


# ----------------------------------------
# Function to find numbers above average
# ----------------------------------------

def numbers_above_average(numbers, average):

    # Create an empty list
    # to store numbers above the average
    result = []

    # Check each number in the list
    for num in numbers:

        # If the number is greater than the average
        if num > average:

            # Add that number to the result list
            result.append(num)

    # Return the list of numbers above average
    return result


# ----------------------------------------
# Get numbers from the user
# ----------------------------------------

# Ask the user to enter numbers separated by spaces
user_input = input("Enter numbers separated by spaces: ")


# Remove extra spaces from the beginning
# and the end of the input
user_input = user_input.strip()


# Check if the user entered anything
if not user_input:

    print("Please enter at least one number.")

else:

    # Split the input into separate pieces
    # Example:
    # "10 20 30"
    #
    # becomes:
    # ["10", "20", "30"]
    number_texts = user_input.split()


    # Create an empty list to store the numbers
    numbers = []


    # Convert each piece of text into an integer
    for text in number_texts:

        # Convert the text to an integer
        number = int(text)

        # Add the number to our list
        numbers.append(number)


    # ----------------------------------------
    # Analyze the numbers
    # ----------------------------------------

    # Send the numbers to the analyze_numbers()
    # function
    total, average, highest, lowest, even_count, odd_count = analyze_numbers(
        numbers
    )


    # ----------------------------------------
    # Display the results
    # ----------------------------------------

    print("\n----- Number Analysis -----")

    print("Sum of Numbers:", total)

    print("Average:", f"{average:.2f}")

    print("Highest Number:", highest)

    print("Lowest Number:", lowest)

    print("Even Number Count:", even_count)

    print("Odd Number Count:", odd_count)


    # ----------------------------------------
    # Find numbers above the average
    # ----------------------------------------

    above_average = numbers_above_average(
        numbers,
        average
    )


    # Display the numbers above the average
    print("Numbers Above Average:", above_average)
