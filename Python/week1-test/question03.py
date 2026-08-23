# ----------------------------------------
# Store course enrollment information
# ----------------------------------------

# A dictionary stores the course name
# together with the number of enrolled students

courses = {
    "Python": 25,
    "Java": 18,
    "SQL": 30,
    "Web": 15
}


# ----------------------------------------
# Display all courses
# ----------------------------------------

print("Course Enrollments:")

# .items() gives us both the course name
# and the number of students
for course, enrollment in courses.items():
    print(f"{course}: {enrollment}")


# ----------------------------------------
# Search for a course
# ----------------------------------------

# Ask the user to enter a course name
course_name = input("\nEnter course name: ")

# Remove extra spaces and make the first
# letter of each word uppercase
course_name = course_name.strip().title()


# Check if the course exists in the dictionary
if course_name in courses:

    # Get the enrollment number using the course name
    enrollment = courses[course_name]

    print("Current Enrollment:", enrollment)

else:
    print("Course not found.")


# ----------------------------------------
# Calculate total enrollments
# ----------------------------------------

# courses.values() gives us all enrollment numbers
# sum() adds all of them together
total_enrollments = sum(courses.values())


# ----------------------------------------
# Find the course with highest enrollment
# ----------------------------------------

# Start with an empty value
highest_course = ""

# Start the highest enrollment at 0
highest_enrollment = 0

# Check every course in the dictionary
for course, enrollment in courses.items():

    # If this course has more students
    # than our current highest enrollment
    if enrollment > highest_enrollment:

        # Save this course as the highest course
        highest_course = course

        # Save its enrollment number
        highest_enrollment = enrollment


# ----------------------------------------
# Find the course with lowest enrollment
# ----------------------------------------

# Start with an empty value
lowest_course = ""

# We need a starting value that is bigger
# than any enrollment number in our dictionary
lowest_enrollment = float("inf")


# Check every course
for course, enrollment in courses.items():

    # If this course has fewer students
    # than our current lowest enrollment
    if enrollment < lowest_enrollment:

        # Save this course as the lowest course
        lowest_course = course

        # Save its enrollment number
        lowest_enrollment = enrollment


# ----------------------------------------
# Find courses with more than 20 students
# ----------------------------------------

# Create an empty list
more_than_20 = []

# Check every course
for course, enrollment in courses.items():

    # Check if enrollment is greater than 20
    if enrollment > 20:

        # Add the course name to the list
        more_than_20.append(course)


# ----------------------------------------
# Display final results
# ----------------------------------------

print("\n----- Course Analysis -----")

print("Total Enrollments:", total_enrollments)

print("Course with Highest Enrollment:", highest_course)

print("Course with Lowest Enrollment:", lowest_course)

print("Courses Having More Than 20 Students:", more_than_20)
