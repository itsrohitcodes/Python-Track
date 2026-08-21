# Add a has_skill method to StudentProfile class

# Define a class named StudentProfile
class StudentProfile:
    # Define the constructor to initialize student attributes
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

    def has_skill(self, skill_name):
        # Search for skill_name and return True or False
        for skill in self.skills:
            if skill.lower() == skill_name.lower():
                return True

        return False

# Take input from the user
student_id = int(input())
name = input().strip()
course = input().strip()
score = float(input())
skills_input = input().strip()
placement_input = input().strip()
skill_to_find = input().strip()

skills = [
    skill.strip()
    for skill in skills_input.split(",") 
    if skill.strip()
]

is_placed = placement_input.lower()

# Create one StudentProfile object
student = StudentProfile(student_id, name, course, score, skills, is_placed)

# Call has_skill() and print the required result
result = student.has_skill(skill_to_find)

if result is True:
    print("Skill Found")
else:
    print("Skill Not Found")