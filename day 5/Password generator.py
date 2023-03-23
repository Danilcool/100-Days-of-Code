#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

unfinished_password = []

for number in range(0,nr_letters):
    random_number = random.randint(0,nr_letters)
    unfinished_password.append(letters[random_number])


for number in range(0,nr_symbols):
    random_number = random.randint(0,nr_symbols)

    unfinished_password.append(symbols[random_number])

for number in range(0, nr_numbers):
    random_number = random.randint(0, nr_numbers)

    unfinished_password.append(numbers[random_number])


finished_password = ""


print(unfinished_password)


random.shuffle(unfinished_password)
print(unfinished_password)

for letter in unfinished_password:
    finished_password += letter

print(finished_password)
