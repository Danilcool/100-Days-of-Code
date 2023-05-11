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

def get_order():
    menu_list = []
    for item in MENU:
        menu_list.append(item)
    print('What Is your Oder:')
    print(menu_list)

    user_choice = input('What is your order')
    while user_choice not in menu_list:
        print('Sorry Try again:')
        print(menu_list)
        user_choice = input('What is your order')
    return user_choice


def make_drink(user_choice,resources):

    if user_choice == 'espresso': and resources["water"] >= 100 and resources["milk"] >= 50 and resources["coffee"] >= 20:



def get_order():


get_order()
