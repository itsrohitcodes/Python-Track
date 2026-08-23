# ----------------------------------------
# Get student information
# ----------------------------------------

# Ask the user to enter the student's name
student_name = input("Enter student name: ")

# Create an empty list to store the marks
marks = []


# ----------------------------------------
# Get marks for 5 subjects
# ----------------------------------------

# Repeat the loop 5 times
for subject in range(5):

    # Ask the user to enter a mark
    mark = int(input("Enter mark: "))

    # Add the mark to the marks list
    marks.append(mark)


# ----------------------------------------
# Calculate basic mark information
# ----------------------------------------

# Add all the marks together
total_marks = sum(marks)

# Find the average mark
# len(marks) tells us how many marks are in the list
average_marks = total_marks / len(marks)

# Find the highest mark
highest_mark = max(marks)

# Find the lowest mark
lowest_mark = min(marks)


# ----------------------------------------
# Count passed and failed subjects
# ----------------------------------------

# Start both counters at 0
passed = 0
failed = 0

# Check each mark in the marks list
for mark in marks:

    # A mark of 40 or more means the student passed
    if mark >= 40:
        passed = passed + 1

    # A mark below 40 means the student failed
    else:
        failed = failed + 1


# ----------------------------------------
# Calculate the final grade
# ----------------------------------------

# Check the average and decide the grade

if average_marks >= 90:
    grade = "A"

elif average_marks >= 75:
    grade = "B"

elif average_marks >= 60:
    grade = "C"

elif average_marks >= 40:
    grade = "D"

else:
    grade = "F"


# ----------------------------------------
# Display student information
# ----------------------------------------

print("\n----- Student Result -----")

print("Student Name:", student_name)
print("Total Marks:", total_marks)
print("Average Marks:", f"{average_marks:.2f}")
print("Highest Mark:", highest_mark)
print("Lowest Mark:", lowest_mark)
print("Subjects Passed:", passed)
print("Subjects Failed:", failed)
print("Final Grade:", grade)


# ----------------------------------------
# Find marks greater than the average
# ----------------------------------------

print("\nMarks greater than average:")

# Check every mark in the list
for mark in marks:

    # Print the mark if it is greater than the average
    if mark > average_marks:
        print(mark)
