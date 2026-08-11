# Calculate weekly study hours using a function

# Create and call display_study_hours() function
def display_study_hours():
    # Read the inputs, calculate the total and print it
    study_hours = int(input())
    study_days = int(input())
    total_study_hours = study_hours * study_days
    print(f"Total Study Hours: {total_study_hours}")

# Call the function
display_study_hours()