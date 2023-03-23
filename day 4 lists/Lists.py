rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
#Write your code below this line 👇

user_choice = input("Rock, Paper or Scissors").lower()

if user_choice == 'rock':
    user_choice = rock
elif user_choice == "paper":
    user_choice = paper
else:
    user_choice = scissors

computer_choice = random.randint(0,2)
print(user_choice)
if computer_choice == 0:
    computer_choice = rock
elif computer_choice == 1:
    computer_choice = paper
elif computer_choice == 2:
    computer_choice = scissors

print(computer_choice)

if computer_choice == user_choice:
    print("   ITS A DRAW")
else:

    if user_choice == rock:
        if computer_choice == paper:
            print("Computer wins")
        else:
            print("You win")


    if user_choice == paper:

        if computer_choice == rock:
            print("You Win")
        else:
            print("Computer wins")

    if user_choice == scissors:

        if computer_choice == rock:
            print("Computer Wins")
        else:
            print("You win")