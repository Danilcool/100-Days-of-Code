#Step 1

word_list = ["aardvark", "baboon", "camel"]
lives = 4

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
import random


random_number = random.randint(1,len(word_list)-1)
chosen_word = word_list[random_number]

secret_word = []
for i in range(len(chosen_word)):
    secret_word += "_"

user_success = 0


while lives != 0 and user_success != len(secret_word):
    print(secret_word)
    user_guess = input('What is your guess:')

    if user_guess in chosen_word:
        print('Correct')

        for number in range(len(chosen_word)):
            letter = chosen_word[number]
            if letter == user_guess:
                secret_word[number] = user_guess
                user_success += 1




    else:
        print('incorrect')
        lives -= 1
        print(lives)




