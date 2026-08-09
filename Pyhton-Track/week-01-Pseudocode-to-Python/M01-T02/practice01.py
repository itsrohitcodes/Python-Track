# Build a Student Grade  calculator

# take marks from user as an input
marks = int(input("Enter marks: "))

# Check whether the marks are valid and display the grade
if marks >= 90 and marks <= 100: 
    print("Grade: A")
elif marks >= 75 and marks <= 89: 
    print("Grade: B")
elif marks >= 60 and marks <= 74: 
    print("Grade: C")
elif marks >= 40 and marks <= 59: 
    print("Grade: D")
elif marks >= 0 and marks <= 39: 
    print("Grade: F")
else:
    print("Invalid Marks")