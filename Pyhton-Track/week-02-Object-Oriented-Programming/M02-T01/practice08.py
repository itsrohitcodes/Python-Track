# Build a Validate Job Opening Class

class JobOpening:
    # Add the constructor, properties and update method here
    def __init__(self, role, minimum_salary, maximum_salary):
        self.role = role
        self.__minimum_salary = minimum_salary
        self.__maximum_salary = maximum_salary

    @property
    def minimum_salary(self):
        return self.__minimum_salary

    @property
    def maximum_salary(self):
        return self.__maximum_salary

    def update_salary_range(self, new_minimum, new_maximum):
        if 0 <= new_minimum < self.__maximum_salary:
            self.__minimum_salary = new_minimum
            self.__maximum_salary = new_maximum

# take input for role, minimum_salary, maximum_salary, new_minimum and new_maximum
role = input().strip()
minimum_salary = int(input())
maximum_salary = int(input())
new_minimum = int(input())
new_maximum = int(input())

# create a JobOpening object
job = JobOpening(role, minimum_salary, maximum_salary)
job.update_salary_range(new_minimum, new_maximum)

# print the job details
print(f"Role: {job.role}")
print(f"Salary Range: {job.minimum_salary} - {job.maximum_salary}")