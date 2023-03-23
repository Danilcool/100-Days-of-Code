#
#
# new_list = [new_item for item in list]

#
# list_of_numbers = [1, 2, 3, 4, 5]
#
# new_list = [number / 2 for number in list_of_numbers]
#
# print(new_list)
#
# string = "angela"
#
# new_list = [letter for letter in string]
# # print(new_list)
#
# range(1,5)
#
# new_list = [number for number in range(1,5+1)]
#
# print(new_list)
# #
# names = ['Danil',"Slava",'Vecheslav']
#
# new_list = [name.upper() for name in names if len(name) > 5]
# print(new_list)

# Dictionary comprehension
# import random
# names = ['Danil',"Slava",'Vecheslav']
#
# student_scores = {
#     "Alex": 98,
#
# }
# new_dic = {student:random.randint(1,101) for student in names}
# print(new_dic)
#
# passed_student = {student:score for (student,score) in new_dic.items() if int(score) > 80}
# print(passed_student)
#
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆
#
# # Write your code below:
#
# result = {word:len(word) for (word) in sentence.split()}
#
# print(result)
#
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# # 🚨 Don't change code above 👆
# weather_f = {day:(temp*9/5)+32 for (day, temp) in weather_c.items()}
#
# # Write your code 👇 below:
#
#
#
# print(weather_f)
#
# student_dic = {
#     "student": ['Danil', 'Slava',"ekaterina"],
#     "score": [57,34,98]
#
# }
#
#
# import pandas
#
# new_data = pandas.DataFrame(student_dic)
# # print(new_data)
#
# for (index,row) in new_data.iterrows():
#     if row.student == "Danil":
#         print(row.score, row.student)




