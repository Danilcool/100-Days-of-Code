import random
def main():

    random_number = get_random_number()
    lifes = get_difficulty()
    print(random_number,lifes)
    player_guess = int(input('What is your guess'))
    get_number_cheaker(random_number, lifes, player_guess)


def get_difficulty():
    user_input = input('Hard or Easy').lower()
    print(user_input)
    user_choice = ['hard','easy']
    while user_input not in user_choice:
        user_input = input('Hard or Easy').lower()

    if user_input == 'hard':
        lifes = 5
        return lifes
    else:
        lifes = 10
        return lifes


def get_random_number():
    return random.randint(1,100)

def get_number_cheaker(random_number,lifes,player_guess):

    while lifes > 0:
        if player_guess != random_number:
            if player_guess > random_number:
                print('Too High')
                lifes -= 1
                print(f'You have {lifes} left')
                player_guess = int(input('What is your Guess:'))

            elif player_guess < random_number:
                print('Too Low')
                lifes -= 1
                print(f'You have {lifes} left')
                player_guess = int(input('What is your Guess:'))
        if player_guess == random_number:
            print('Congradulations')
            print(f"Thats correct the number was: {random_number}")
            break
    else:
        print(f'You lost the Correct answer was: {random_number}')


main()