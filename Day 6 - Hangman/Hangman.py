#Step 1

word_list = ["aardvark", "baboon", "camel"]
lives = 4

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
import random

random_number = random.randint(0,len(word_list)) - 1
playing_word = word_list[random_number]
secret_word = []

word_length = len(playing_word)


for number in range(word_length):
    secret_word += "_"
print(secret_word)

win_count = len(playing_word)
player_correct_words_count = 0


while lives != 0:
    if player_correct_words_count == win_count:
        print('you win the game')
        break

    player_guess = input("Whats your letter").lower()


    if player_guess in playing_word:

        for position in range(word_length):
            letter = playing_word[position]
            if letter == player_guess:
                secret_word[position] = player_guess
                player_correct_words_count += 1

            else:
                pass
        print(secret_word)

    else:
        print("incorrect")
        print(secret_word)
        lives -= 1
        print(f"You have {lives} left")


else:
    print('You lost the game')

