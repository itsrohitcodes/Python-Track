# Encapsulate required skills in JobDescription class

class JobDescription:
    # Add the constructor, property and method here
    def __init__(self, role, skills):
        self.role = role
        self.__required_skills = skills

    @property
    def required_skills(self):
        return self.__required_skills

    def add_required_skill(self, new_skill):
        if new_skill not in self.__required_skills:
            self.__required_skills.append(new_skill)

# take input for role, skills and new_skill
role = input().strip()
skills = [skill.strip() for skill in input().split(",")]
new_skill = input().strip()

# create a JobDescription object
job = JobDescription(role, skills)
job.add_required_skill(new_skill)

# print the job details
print(f"Job Role: {job.role}")
print(f"Required Skills: {', '.join(job.required_skills)}")