# Create a Placement Manager with Object Collections

# Define the StudentProfile class to store student information
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

        # Assign values
        self.student_id = student_id
        self.name = name
        self.course = course
        self.score = score
        self.skills = list(skills)
        self.is_placed = is_placed


# Define the JobDescription class to store job information
class JobDescription:
    def __init__(
        self,
        job_id,
        company,
        role,
        location = "Remote",
        minimum_score = 0.0,
        required_skills = None,
        is_active = True
    ):

        # Assign values
        self.job_id = job_id
        self.company = company
        self.role = role
        self.location = location
        self.minimum_score = minimum_score
        self.required_skills = (
            []
            if required_skills is None
            else list(required_skills)
        )
        self.is_active = is_active


# Define the PlacementManager class to manage student and job collections
class PlacementManager:
    def __init__(self):
        # Create separate empty collections for students and jobs
        self.student_profiles = []
        self.job_descriptions = []


# Input student data
student_id = int(input())
name = input().strip()
course = input().strip()
score = float(input())
skills_input = input().strip()
placement_input = input().strip()

# Input job data
job_id = int(input())
company = input().strip()
role = input().strip()
location = input().strip()
minimum_score = float(input())
required_skills_input = input().strip()
job_status_input = input().strip()

# Process skills from input string to list
skills = [
    skill.strip() for skill in skills_input.split(",") if skill.strip()
]

# Process required skills from input string to list
required_skills = [
    skill.strip() for skill in required_skills_input.split(",") if skill.strip()
]

# Convert placement status to boolean
is_placed = placement_input.lower() == "yes"

# Convert job status to boolean
is_active = job_status_input.lower() == "yes"

# Create student and job objects
student = StudentProfile(
    student_id,
    name,
    course,
    score,
    skills,
    is_placed
)

# Create job object
job = JobDescription(
    job_id,
    company,
    role,
    location,
    minimum_score,
    required_skills,
    is_active
)

# Create exactly one PlacementManager object
manager = PlacementManager()

# Store the complete student and job objects
manager.student_profiles.append(student)
manager.job_descriptions.append(job)

# Print the collection sizes and stored-record summaries
print(f"Student Profiles: {len(manager.student_profiles)}")
print(f"Job Descriptions: {len(manager.job_descriptions)}")
print(
    f"Stored Student: {manager.student_profiles[0].student_id} - {manager.student_profiles[0].name}"
)
print(
    f"Stored Job: {manager.job_descriptions[0].job_id} - {manager.job_descriptions[0].role}"
)