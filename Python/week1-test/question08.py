# ----------------------------------------
# Function to compare student skills
# with required skills
# ----------------------------------------

def match_skills(student_skills, required_skills):

    # Create a set containing skills
    # that are present in both sets
    matched_skills = student_skills.intersection(required_skills)


    # Find the required skills that the
    # student does not have
    missing_skills = required_skills.difference(student_skills)


    # Find the skills the student has
    # that are not required
    extra_skills = student_skills.difference(required_skills)


    # ----------------------------------------
    # Calculate match percentage
    # ----------------------------------------

    # Make sure the required skills set
    # is not empty before dividing
    if required_skills:

        # Calculate how many required skills
        # the student has
        matched_count = len(matched_skills)

        # Calculate how many skills are required
        required_count = len(required_skills)

        # Calculate the percentage
        match_percentage = (
            matched_count / required_count
        ) * 100

    else:

        # If there are no required skills,
        # set the percentage to 0
        match_percentage = 0


    # Return all the results
    return (
        matched_skills,
        missing_skills,
        extra_skills,
        match_percentage
    )


# ----------------------------------------
# Get student's skills
# ----------------------------------------

print("Enter student skills separated by spaces:")

student_input = input()


# Split the input into individual skills
student_skill_list = student_input.split()


# Create an empty set
student_skills = set()


# Add each skill to the set
for skill in student_skill_list:

    # Convert the skill to lowercase
    # before adding it
    skill = skill.lower()

    student_skills.add(skill)


# ----------------------------------------
# Get required skills
# ----------------------------------------

print("Enter required skills separated by spaces:")

required_input = input()


# Split the input into individual skills
required_skill_list = required_input.split()


# Create an empty set
required_skills = set()


# Add each required skill to the set
for skill in required_skill_list:

    # Convert the skill to lowercase
    skill = skill.lower()

    required_skills.add(skill)


# ----------------------------------------
# Compare the skills
# ----------------------------------------

matched_skills, missing_skills, extra_skills, match_percentage = match_skills(
    student_skills,
    required_skills
)


# ----------------------------------------
# Decide the student's status
# ----------------------------------------

# If the student has at least 70% of
# the required skills, they are eligible
if match_percentage >= 70:

    status = "Eligible"

else:

    status = "Needs More Skills"


# ----------------------------------------
# Display the results
# ----------------------------------------

print("\n----- Skill Analysis -----")

print("Student Skills:", student_skills)

print("Required Skills:", required_skills)

print("Matched Skills:", matched_skills)

print("Missing Skills:", missing_skills)

print("Extra Skills:", extra_skills)

print(f"Match Percentage: {match_percentage:.2f}%")

print("Status:", status)
