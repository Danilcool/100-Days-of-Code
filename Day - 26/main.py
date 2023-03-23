# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass
#
# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}
#
# #TODO 1. Create a dictionary in this format:
# dic = {"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

file = open("nato_phonetic_alphabet.csv")
import pandas

file_panda = pandas.read_csv("nato_phonetic_alphabet.csv")


dic = {row.letter:row.code for (index,row) in file_panda.iterrows() if row.letter == row.code[0]}
print(dic)

user_input = input('Word').upper()

new_dic = {dic[letter]:letter for letter in user_input}
print(new_dic)

