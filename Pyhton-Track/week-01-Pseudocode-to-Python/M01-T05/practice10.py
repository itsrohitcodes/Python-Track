# Search Profiles and Jobs by ID

# Define the StudentProfile class to store student information
class StudentProfile:
    # Constructor to initialize student data
    def __init__(self, student_id, name, course):
        self.student_id = student_id
        self.name = name
        self.course = course

    # Override __str__ method for easy printing
    def __str__(self):
        return f"{self.student_id} - {self.name} - {self.course}"


# Define the JobDescription class to store job information
class JobDescription:
    # Constructor to initialize job data
    def __init__(self, job_id, company, role):
        self.job_id = job_id
        self.company = company
        self.role = role

    # Override __str__ method for easy printing
    def str_(self):
        return f"{self.job_id} - {self.company} - {self.role}"


# Define the PlacementManager class to manage student and job collections
class PlacementManager:
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
        self.job_descriptions.append(job_description)

    # Method to find a student by ID
    def find_student_by_id(self, student_id):
        # Iterate through the student profiles
        for student in self.student_profiles:
            if student.student_id == student_id:
                return student
        return None

    # Method to find a job by ID
    def find_job_by_id(self, job_id):
        # Iterate through the job descriptions
        for job in self.job_descriptions:
            if job.job_id == job_id:
                return job
        return None

# Create a PlacementManager object
manager = PlacementManager()

# Input and store student data
student_count = int(input())

# Loop through the student data
for _ in range(student_count):
    student_id = int(input())
    name = input().strip()
    course = input().strip()

    # Create student object
    student = StudentProfile(student_id, name, course)

    # Add the student through the manager method
    manager.add_student_profile(student)


# Input and store job data
job_count = int(input())

# Loop through the job data
for _ in range(job_count):
    job_id = int(input())
    company = input().strip()
    role = input().strip()

    # Create job object
    job = JobDescription(job_id, company, role) 

    # Add the job through the manager method
    manager.add_job_description(job)

# Input the student and job IDs to search for
student_id_to_find = int(input())
job_id_to_find = int(input())

# Search for the student and job

result_student = manager.find_student_by_id(student_id_to_find)
result_job = manager.find_job_by_id(job_id_to_find)

# Display the search results
if result_student is not None:
    print(f"Student Found: {result_student}")
else:
    print("Student Not Found")

if result_job is not None:
    print(f"Job Found: {result_job}")
else:
    print("Job Not Found")