MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def main():
    user_choice = get_user_valid_input()
    users_money = get_coins()

    while user_choice != 'stop':
        if user_choice == "report":
            print(f"Water:{resources['water']}ml\n"
                  f"Milk:{resources['milk']}ml\n"
                  f"Coffe:{resources['coffee']}ml\n"
                  f"Money:{resources['money']}")
            user_choice = get_user_valid_input()
        elif user_choice == "espresso" and users_money >= 1.5:
            get_drink(user_choice)
            get_change(users_money, user_choice)
            user_choice = get_user_valid_input()
        elif user_choice == "latte" and users_money >= 2.5:
            get_drink(user_choice)
            get_change(users_money, user_choice)
            user_choice = get_user_valid_input()
        elif user_choice == "cappuccino" and users_money >= 3.0:
            get_drink(user_choice)
            get_change(users_money, user_choice)
            user_choice = get_user_valid_input()
        else:
            print('You dont have enouth money')



def get_user_valid_input():
    user_choice = input("What whould you like (espresso,latte,cappuccino)").lower()
    machine_option = ["stop",'report','espresso','latte','cappuccino']
    while user_choice not in machine_option:
        print('Invalid please try again')
        user_choice = get_user_valid_input()
    return user_choice


def get_espresso():
    espresso = MENU["espresso"]
    espresso_inredients = espresso['ingredients']
    if resources["water"] > espresso_inredients['water']:
            if resources["coffee"] > espresso_inredients['coffee']:
                resources["water"] -= espresso_inredients['water']
                resources["coffee"] -= espresso_inredients['coffee']
                resources['money'] += espresso['cost']
                print(resources)
            else:
                print("The Machine does not have enouth Water")
    else:
        print("The Machine does not have enouth Water")

def get_cappuccino():
    cappuccino = MENU["cappuccino"]
    cappuccino_inredients = cappuccino['ingredients']
    if resources["water"] > cappuccino_inredients['water']:
            if resources["coffee"] > cappuccino_inredients['coffee']:
                if resources["milk"] > cappuccino_inredients['milk']:
                    resources["water"] -= cappuccino_inredients['water']
                    resources["coffee"] -= cappuccino_inredients['coffee']
                    resources["milk"] -= cappuccino_inredients['milk']
                    resources['money'] += cappuccino['cost']
                    print(resources)
                else:
                    print("The Machine does not have enouth Milk")
            else:
                print("The Machine does not have enouth Water")
    else:
        print("The Machine does not have enouth Water")

def get_latte():
    latte = MENU["latte"]
    latte_inredients = latte['ingredients']
    if resources["water"] > latte_inredients['water']:
            if resources["coffee"] > latte_inredients['coffee']:
                if resources["milk"] > latte_inredients['milk']:
                    resources["water"] -= latte_inredients['water']
                    resources["coffee"] -= latte_inredients['coffee']
                    resources["milk"] -= latte_inredients['milk']
                    resources['money'] += latte['cost']
                    print('Here is your latte')
                else:
                    print("The Machine does not have enouth Milk")
            else:
                print("The Machine does not have enouth Water")
    else:
        print("The Machine does not have enouth Water")


def get_coins():
    qurters = int(input("How many Quarters?:"))
    dimes = int(input("How many Dimes?:"))
    nickels = int(input("How many Nickels?:"))
    pennies = int(input("How many Pennies?:"))
    total = (qurters * 0.25) + (dimes + 0.10) + (nickels + 0.05) + (pennies * 0.01)
    return total

def get_change(users_money,user_choice):
    menu_iteam = MENU[user_choice]
    users_money -= menu_iteam['cost']
    print(f'Sir your change is {users_money:.2f}')
    return users_money


def get_drink(user_choice):
    drink = MENU[user_choice]
    drink_ingredients = drink['ingredients']
    if resources["water"] > drink_ingredients['water']:
            if resources["coffee"] > drink_ingredients['coffee']:
                resources["water"] -= drink_ingredients['water']
                resources["coffee"] -= drink_ingredients['coffee']
                resources['money'] += drink['cost']
                print(resources)
            else:
                print("The Machine does not have enouth Water")
    else:
        print("The Machine does not have enouth Water")

main()