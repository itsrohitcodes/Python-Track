# Protect a Read only Application ID

class CandidateApplication:
    # Add the constructor and read-only property here
    def __init__(self, application_id, candidate_name):
        self.__application_id = application_id
        self.candidate_name = candidate_name

    @property
    def application_id(self):
        return self.__application_id

# take input for application_id and candidate_name
application_id = input().strip()
candidate_name = input().strip()

# create a CandidateApplication object
application = CandidateApplication(application_id, candidate_name)

# print the application details
print(f"Application ID: {application.application_id}")
print(f"Candidate Name: {application.candidate_name}")