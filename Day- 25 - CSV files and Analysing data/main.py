# with open("weather_data.csv",'r') as file:
#     containts = file.readlines()
#     print(containts)

#
# import csv
#
# temperetures = []
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#
#     for row in data:
#         if row[1] != 'temp':
#
#             temperetures.append(row[1])
# print(temperetures)

import pandas

data = pandas.read_csv("weather_data.csv")

data_dict= data.to_dict()



temp_list = data['temp'].to_list()




total = 0
for number in temp_list:
    total += int(number)
average = total/len(temp_list)


#Getting data in row

highest_temp = data.temp.max()
# print(highest_temp)
#
# print(data[data.temp == data.temp.max()])


monday = data[data.day == 'Monday']
monday_tempreture_far = monday.temp * 1.8 +32
#
# print(monday_tempreture_far)

# Create a data Frame from Scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv('new_data.csv')

