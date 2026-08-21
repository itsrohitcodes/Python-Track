# Add and Display Student Profiles and Jobs

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

    # Override __str__ method for easy printing
    def __str__(self):
        return f"{self.student_id} - {self.name} - {self.course}"


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

    # Override __str__ method for easy printing
    def __str__(self):
        return f"{self.job_id} - {self.company} - {self.role}"



# Define the PlacementManager class to manage student and job collections
class PlacementManager:
    # Constructor to initialize empty collections
    def __init__(self):
        # Initialize empty collections for students and jobs
        self.student_profiles = []
        self.job_descriptions = []
    
    # Method to add a complete student object
    def add_student_profile(self, student_profile): 
        # Add the complete student object 
        self.student_profiles.append(student_profile)

    # Method to add a complete job object
    def add_job_description(self, job_description): 
        # Add the complete job object 
        self.job_descriptions.append(job_description)

    # Method to display all student profiles
    def display_student_profiles(self):
        # Display the heading, records or empty message
        if len(self.student_profiles) == 0: 
            print("STUDENT PROFILES") 
            print("No student profiles available")
        else:
            print("STUDENT PROFILES")
            for student in self.student_profiles:
                print(f"{student.student_id} - {student.name} - {student.course}")

    # Method to display all job descriptions
    def display_job_descriptions(self):
        # Display the heading, records or empty message 
        if len(self.job_descriptions) == 0: 
            print("JOB DESCRIPTIONS") 
            print("No job descriptions available")
        else:
            print("JOB DESCRIPTIONS")
            for job in self.job_descriptions:
                print(f"{job.job_id} - {job.company} - {job.role}")


# Create a PlacementManager object
manager = PlacementManager()

# Input and store student data
student_count = int(input())

for _ in range(student_count):
    student_id = int(input())
    name = input().strip()
    course = input().strip()
    score = float(input())
    skills_input = input().strip()
    placement_input = input().strip()

    # Process skills from input string to list
    skills = [
        skill.strip() for skill in skills_input.split(",") if skill.strip()
    ]
    
    # Convert placement status to boolean
    is_placed = placement_input.lower() == "yes"

    # Create student object
    student = StudentProfile(
        student_id,
        name,
        course,
        score,
        skills,
        is_placed
    )

    # Add the student through the manager method
    manager.add_student_profile(student)

# Input and store job data
job_count = int(input())

for _ in range(job_count):
    job_id = int(input())
    company = input().strip()
    role = input().strip()
    location = input().strip()
    minimum_score = float(input())
    required_skills_input = input().strip()
    job_status_input = input().strip()

    # Process required skills from input string to list
    required_skills = [
        skill.strip() for skill in required_skills_input.split(",") if skill.strip()
    ]
    
    # Convert job status to boolean
    is_active = job_status_input.lower() == "yes"

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
    # Add the job through the manager method
    manager.add_job_description(job)

# Display all student and job records
manager.display_student_profiles()
manager.display_job_descriptions()