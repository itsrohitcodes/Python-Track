# Validate Student score using a property setter

class StudentProfile:
    def __init__(self, score):
        self.__score = 0
        # Assign the score using the property

    @property
    def score(self):
        # Return the stored score
        return self.__score

    @score.setter
    def score(self, new_score):
        # Validate and store the score
        if 0 <= new_score <= 100 :
            self.__score = new_score

# take input for score
score = int(input())

# create a StudentProfile object
student = StudentProfile(score)
student.score = score

# print the student details
print(f"Score: {student.score}")