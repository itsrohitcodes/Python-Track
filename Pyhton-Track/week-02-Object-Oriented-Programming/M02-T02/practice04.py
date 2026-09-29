# Build a Candidate Profile Factory Method

class CandidateProfile:
    def __init__(self, name, skill, experience):
        self.name = name
        self.skill = skill
        self.experience = experience

    @classmethod
    def from_string(cls, data):
        # Complete the factory method
        name, skill, experience = data.split(",")

        return cls(name, skill, experience)


data = input().strip()
candidate = CandidateProfile.from_string(data)

print(f"Name: {candidate.name}")
print(f"Skill: {candidate.skill}")
print(f"Experience: {candidate.experience}")