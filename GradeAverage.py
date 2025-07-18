
# GradeAverage.py

# Get number of subjects
num_subjects = int(input("Enter the number of subjects: "))

# Initialize total
total = 0

# Get grades for each subject
for i in range(1, num_subjects + 1):
    grade = float(input(f"Enter grade for subject {i}: "))
    total += grade

# Calculate average
average = total / num_subjects

# Determine letter grade
if average >= 90:
    grade_letter = "A"
elif average >= 80:
    grade_letter = "B"
elif average >= 70:
    grade_letter = "C"
elif average >= 60:
    grade_letter = "D"
else:
    grade_letter = "F"

# Display results
print(f"\nTotal Marks: {total}")
print(f"Average: {average:.2f}")
print(f"Grade: {grade_letter}")

