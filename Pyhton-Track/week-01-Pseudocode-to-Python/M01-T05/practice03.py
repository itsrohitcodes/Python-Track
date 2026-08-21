# Create a Student profile from user input

# Define a class named StudentProfile with constructor
class StudentProfile:
    def __init__(
        self,
        student_id,
        name,
        course,
        score,
        skills,
        is_placed
    ):
        # Store all received values in instance attributes
        self.student_id = student_id
        self.name = name
        self.course = course
        self.score = score
        self.skills = skills
        self.is_placed = is_placed

# Take input from the user
student_id = int(input())
name = input().strip()
course = input().strip()
score = float(input())
skills_input = input().strip()
placement_input = input().strip()

# Convert skills input into a list of skill names
skills = []
skills.append(skills_input)

# Convert placement_input into a Boolean value
if placement_input.lower() == "yes":
    is_placed = True
else:
    is_placed = False

# Create one StudentProfile object
student = StudentProfile(student_id, name, course, score, skills, is_placed)

# Print the stored student details
print(f"Student ID: {student.student_id}")
print(f"Name: {student.name}")
print(f"Course: {student.course}")
print(f"Score: {student.score}")
print(f"Skills: {', '.join(student.skills)}")

if student.is_placed == True:
    status = "Placed"
else:
    status = "Not Placed"

print(f"Placement Status: {status}")