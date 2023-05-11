

def main():

    user_number_one = int(input('N1:'))
    user_action = get_user_input()
    user_number_two = int(input('N2:'))

    result = calculate(user_number_one,user_number_two,user_action)
    print(result)


def get_user_input():

    user_choices = ['-',"+","*",'/']
    print(f'User Choice:{user_choices}')
    user_input = input()

    while user_input not in user_choices:
        print('Sorry Please try again')
        print(user_input)
        user_input = input()
    return user_input


def calculate(user_number_one,user_number_two,user_action):

    print(user_action)
    if user_action == "+":
        return user_number_one + user_number_two
    elif user_action == "-":
        return user_number_one - user_number_two
    elif user_action == "*":
        return user_number_one * user_number_two
    elif user_action == "/":
        return user_number_one / user_number_two

main()