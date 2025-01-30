from art import logo

# print("Hello")
# print("\n" * 100)
# # --> prints x number of new lines
# print("Print something")

print(logo)
# TODO-1: Ask the user for input
# name = input("What is your name? ")
# price = float(input("What is your bid? $"))

# TODO-2: Save data into dictionary {name: price}
# bids[name] = price

# TODO-3: Whether if new bids need to be added
# other_bidders = input("Are there any other bidders? Type 'yes' or 'no'... ")

def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    max(bidding_dictionary)
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}.")

bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name? ")
    price = float(input("What is your bid? $"))
    bids[name] = price
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'... ")
    if other_bidders == 'no':
        continue_bidding = False
        find_highest_bidder(bids)
    elif other_bidders == 'yes':
        print("\n" * 20)


# TODO-4: Compare bids in dictionary (lines 20 - 29)