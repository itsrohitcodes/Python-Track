# Build a Reusable Skill Normalization Utility

class SkillUtility:
    # Create the static method here
    @staticmethod
    def normalize_skill(skill):
        skill = skill.strip().lower()

        return skill


skill = input()

result = SkillUtility.normalize_skill(skill)
print(f"Normalized Skill: {result}")