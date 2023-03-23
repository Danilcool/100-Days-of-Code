student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.


# TODO-2: Write your code below to add the grades to student_grades.👇


# 🚨 Don't change the code below 👇
grades_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        grades_grades[student] = "Outstanding"
    elif score > 80:
        grades_grades[student] = "great"
    else:
        grades_grades[student] = 'fail'

grades_grades['danil'] = 'fail'
print(grades_grades)