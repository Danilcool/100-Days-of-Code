

student_scores = [90,2,0,34,35,54,2123,4,353,2,3434,254,5,2323,3,4]

print(max(student_scores))
biggest_number=0
for number in student_scores:
    if number > biggest_number:
        biggest_number = number
    else:
        pass

print(biggest_number)