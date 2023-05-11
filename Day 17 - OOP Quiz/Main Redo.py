from data import question_data
import random



def main():

    while len(question_data) != 0:

        random_number = get_random_data_string(question_data)
        random_string = question_data[random_number]
        question(random_string,question_data,random_number)



def get_random_data_string(question_data):

    random_number = random.randint(0,len(question_data)-1)
    return random_number


def get_valid_response():
    user_input = input('Is this True or False:').capitalize()

    user_choices = ['True','False']
    while user_input not in user_choices:
        user_input = input('Is this True or False:').capitalize()
    else:
        return user_input


def question(data_string,question_data,random_number):

    print(data_string['text'])
    user_input = get_valid_response()

    if user_input == data_string["answer"]:
        print('Correct')
        question_data.pop(random_number)
        print(len(question_data))
    else:
        print('Incorrect')

main()

