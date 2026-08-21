# Create a StudentProfile Class and Object  

# Define a class named StudentProfile
class StudentProfile:
    def __init__(self, name):
        self.name = name


# Take input in name variable
name = input().strip()

# Create a StudentProfile object
StudentProfile(name)

# Store the name in the object
student = StudentProfile(name)

# Print the stored name
print(f"Student Name: {student.name}")