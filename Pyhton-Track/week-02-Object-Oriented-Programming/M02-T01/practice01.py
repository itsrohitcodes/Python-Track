# Upgrade the StudentProfile using Encapsulation

class StudentProfile:
    # Add the constructor and properties here
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    @property
    def name(self):
        return self.__name

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, new_score):
        if 0 <= new_score <= 100:
            self.__score = new_score


# take input for name, score and new_score
name = input().strip()
score = int(input())
new_score = int(input())

# create a StudentProfile object
student = StudentProfile(name, score)
student.score = new_score

# print the student details
print(f"Student Name: {student.name}")
print(f"Score: {student.score}")