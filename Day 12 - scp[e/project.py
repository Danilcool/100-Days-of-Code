import random



def main():
    random_number = get_random_number()
    lifes = get_difficulty()
    player_guess = int(input('What is your Guess:'))
    get_number_cheaker(random_number, lifes,player_guess)


def get_diffuculty_setting():
    choice_of_user = input('Hard or Easy:').lower()
    choice_options = ['hard','easy']
    while choice_of_user not in choice_options:
        choice_of_user = input('Hard or Easy:').lower()
    if choice_of_user == 'hard':
        guesses = 5
        return guesses
    elif choice_of_user == 'easy':
        guesses = 10
        return guesses

def get_random_number():
    random_number = random.randint(1,100)
    return random_number

def get_number_cheaker(random_number,lifes,player_guess):

    if lifes > 0:
        while player_guess != random_number:
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
    else:
        print(f'You lost the Correct answer was: {random_number}')

main()
