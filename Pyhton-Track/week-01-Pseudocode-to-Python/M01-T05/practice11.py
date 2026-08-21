# Build and Extend the Complete Placement Manager

class StudentProfile:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def __str__(self):
        return f"{self.student_id} - {self.name}"


class JobDescription:
    def __init__(self, job_id, role):
        self.job_id = job_id
        self.role = role

    def __str__(self):
        return f"{self.job_id} - {self.role}"

class PlacementManager:
    def __init__(self):
        self.students = []
        self.jobs = []

    def add_student(self, student):
        self.students.append(student)

    def add_job(self, job):
        self.jobs.append(job)

    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def find_job(self, job_id):
        for job in self.jobs:
            if job.job_id == job_id:
                return job
        return None

manager = PlacementManager()

for _ in range(int(input())):
    student = StudentProfile(int(input()), input().strip()) 
    manager.add_student(student)

for _ in range(int(input())):
    job = JobDescription(int(input()), input().strip())
    manager.add_job(job)

student_id = int(input()) 
job_id = int(input())

# Display collection sizes and search results
student_result = manager.find_student(student_id)
job_result = manager.find_job(job_id)

# Display total number of students and jobs
print(f"Students: {len(manager.students)}") 
print(f"Jobs: {len(manager.jobs)}")

# Display search results
if student_result is not None: 
    print(f"Student: {student_result}")
else:
    print("Student Not Found")

if job_result is not None: 
    print(f"Job: {job_result}")
else:
    print("Job Not Found")