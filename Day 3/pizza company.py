print('Hello welcome to pizza hut ')

print('''
Small :15
Medium :20
Large :30

pepperoni +2$

cheese + 1$

''')
total_pay = 0

choice = input("What pizza size whould you like:").lower()

if choice == "small":
    total_pay += 15
elif choice == "Medium":
    total_pay += 20
else:
    total_pay += 25

peperoni_choice = input("whould you like pepperoni with your pizza (yes or no):").lower()

if peperoni_choice == "yes":
    total_pay +=2

extra_cheese = input("Whould you like extra Cheese (yes or no):")

if extra_cheese == "yes":
    total_pay += 1

print(f"Thank you for your order your final pay is {total_pay}")
