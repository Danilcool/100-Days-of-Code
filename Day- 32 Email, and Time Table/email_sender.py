import pandas
import datetime


birth_days = pandas.read_csv('birthdays.csv')
birth_day_dic = birth_days.to_dict()

print(birth_day_dic)