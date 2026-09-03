# Build a validate Course Enrollment Class

class CourseEnrollment:
    # Add the constructor and status property here
    def __init__(self, student_name, course_name):
        self.student_name = student_name
        self.course_name = course_name
        self.__status = "Enrolled"

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, new_status):
        if new_status == "Enrolled" or new_status == "Completed" or new_status == "Dropped":
            self.__status = new_status

# take input for student_name, course_name and new_status
student_name = input().strip()
course_name = input().strip()
new_status = input().strip()

# create a CourseEnrollment object
enrollment = CourseEnrollment(student_name, course_name)
enrollment.status = new_status

# print the course enrollment details
print(f"Student: {enrollment.student_name}")
print(f"Course: {enrollment.course_name}")
print(f"Status: {enrollment.status}")