def get_calling_of_functions(action,number_one,number_two):

    if action == "+":
        return get_addition(number_one, number_two)

    elif action == "-":
        return get_minus(number_one, number_two)

    elif action == "/":
        return get_divition(number_one, number_two)

    elif action == "*":
        return get_multiplication(number_one, number_two)

def get_addition(number_one,number_two):
    return number_one + number_two

def get_minus(number_one,number_two):
    return number_one - number_two

def get_divition(number_one,number_two):
    return number_one / number_two

def get_multiplication(number_one,number_two):
    return number_one * number_two

def get_choice():
    choices = ("+", "-", "/", "*")
    action = (input('What is your action: '))
    while action not in choices:
        print("Try Again")
        action = (input('What is your action: '))
    else:
        return action

def main():
    number_one = int(input("What is your number"))
    print("+ - / * ?")

    action = get_choice()

    number_two = int(input("What is your number"))

    final_result = get_calling_of_functions(action,number_one,number_two)

    print(f"Result: {number_one} {action} {number_two} = {final_result}")

    print('Whould you like to use this number for diffrent caculation:'
          'Yes or No ')
    continue_or_not = input(":").lower()

    while continue_or_not != "no":
        action = get_choice()
        number_two = int(input("What is your number"))
        final_result = get_calling_of_functions(action, final_result, number_two)
        print(f"Result: {number_one} {action} {final_result} = {final_result}")
    else:
        print("end"
              "")
main()

def get_continue_or_not():
    continue_or_not = input(":").lower()
    while continue_or_not != "no":
        action = get_choice()
        number_two = int(input("What is your number"))
        final_result = get_calling_of_functions(action, final_result, number_two)
        print(f"Result: {number_one} {action} {final_result} = {final_result}")
    else:
        print("end"
              "")