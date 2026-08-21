# Dislay a Student Profile using __str__ method

# Define a class named StudentProfile
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

        self.student_id = student_id
        self.name = name
        self.course = course
        self.score = score
        self.skills = skills
        self.is_placed = is_placed


    def __str__(self):
        # Return the complete formatted student profile
        if is_placed == "yes":
            status = "Placed"
        else:
            status = "Not Placed"

        return(
            f"Student ID: {self.student_id}\n"
            f"Name: {self.name}\n"
            f"Course: {self.course}\n"
            f"Score: {self.score}\n"
            f"Skills: {', '.join(self.skills)}\n"
            f"Placement Status: {status}"
        )    

# Take input from the user
student_id = int(input())
name = input().strip()
course = input().strip()
score = float(input())
skills_input = input().strip()
placement_input = input().strip()

# Convert input skills into a list of strings
skills = [
    skill.strip()
    for skill in skills_input.split(",")
    if skill.strip()
]

is_placed = placement_input.lower()

# Create one StudentProfile object
student = StudentProfile(
    student_id,
    name,
    course,
    score,
    skills,
    is_placed
)

# Display the object using print(student)
print(student)