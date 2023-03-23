

print("Welcome to auction:")
list_of_bidders = {}

yes_or_no = ""
while yes_or_no != 'no':
    name_of_user = input("What is your name: ")
    user_bet = int(input("What is your price"))
    yes_or_no = input("Is there another person")
    list_of_bidders[name_of_user] = user_bet

print(list_of_bidders)


def fund_highest_bidder(list_of_bidders):
    top_bid = 0
    for key in list_of_bidders:
        bid_amount = list_of_bidders[key]
        if bid_amount > top_bid:
            top_bid = bid_amount
            winner = key
    print(top_bid, winner)

fund_highest_bidder(list_of_bidders)


