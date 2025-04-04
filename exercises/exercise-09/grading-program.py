student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

# Scores 91 - 100: Grade = "Outstanding" 
# Scores 81 - 90: Grade = "Exceeds Expectations" 
# Scores 71 - 80: Grade = "Acceptable" 
# Scores 70 or lower: Grade = "Fail" 

student_grades = {}

for student in student_scores:
    print(student)
    if student_scores[student] <= 70:
        student_grades[student] = "Fail"
    elif 71 <= student_scores[student] <= 80:
        student_grades[student] = "Acceptable"
    elif 81 <= student_scores[student] <= 90:
        student_grades[student] = "Exceeds Expectations"
    else:
        student_grades[student] = "Outstanding"

print(student_grades)
