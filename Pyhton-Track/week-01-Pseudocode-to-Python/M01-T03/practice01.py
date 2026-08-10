# Analyze updated marks of students

# Read the number of students
student_count = int(input())
marks = []

# Read and store all marks using append()
for i in range(1, student_count + 1):
    mark = int(input())
    marks.append (mark)

# Read the position, corrected mark and passing mark
position = int(input())
corrected_mark = int(input())
passing_mark = int(input())

# Update the mark at the entered student position
marks [position - 1] = corrected_mark

# Calculate the total, average, highest and lowest marks
total = sum(marks)
average = total / student_count
highest = max(marks)
lowest = min(marks)

# Initialize the count of passed students
passed_students = 0

# Count the students whose marks satisfy the passing condition
for i in marks:
    if i > passing_mark:
        passed_students += 1

# Display the updated analysis
print(f"Updated Marks: {marks}")
print(f"Total Marks: {total}")
print(f"Average Marks: {average}")
print(f"Highest Mark: {highest}")
print(f"Lowest Mark: {lowest}")
print(f"Passed Students: {passed_students}")