# Create a JobDescription class and object

# define a class
class JobDescription:
    # define an initializer with the following parameters
    def __init__(
        self,
        job_id,
        company,
        role,
        location="Remote",
        minimum_score=0.0,
        required_skills=None,
        is_active=True
    ):

        # Store all instance attributes
        self.job_id = job_id
        self.company = company
        self.role = role
        self.location = location
        self.minimum_score = minimum_score
        self.required_skills = required_skills
        self.is_active = is_active


    def __str__(self):
        # Return the complete formatted job description
        if self.is_active == "yes":
            status = "Active"
        else:
            status = "Closed"

        return(
            f"Job ID: {self.job_id}\n"
            f"Company: {self.company}\n"
            f"Role: {self.role}\n"
            f"Location: {self.location}\n"
            f"Minimum Score: {self.minimum_score}\n"
            f"Required Skills: {', '.join(self.required_skills)}\n"
            f"Status: {status}"
        )

# read input from the user
job_id = int(input())
company = input().strip()
role = input().strip()
location = input().strip()
minimum_score = float(input())
skills_input = input().strip()
status_input = input().strip()

# split the skills input by comma and strip the whitespace
required_skills = [
    skill.strip()
    for skill in skills_input.split(",")
    if skill.strip()
]

is_active = status_input.lower()

# Create exactly one JobDescription object
job = JobDescription(
    job_id,
    company,
    role,
    location,
    minimum_score,
    required_skills,
    is_active
)

# Print the object directly
print(job)