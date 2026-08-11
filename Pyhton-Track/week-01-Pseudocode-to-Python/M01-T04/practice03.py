# Pass students details to a function

# Create and call display_student() function
def display_student(name, course):
    # Write your code here
    print(f"Student: {name}")
    print(f"Course: {course}")

# Read inputs and call function
student_name = input()
course_name = input()

# Call the function and pass the inputs as arguments
display_student(student_name, course_name)