import art
import os

os.system('cls')

print(art.logo)

bid_list = {}

while True:
    name = input("What is your name?: ")
    
    while True:
        try:
            bid = float(input("What is your bid?: £"))
            break
        except ValueError:
            print("Please enter a valid number.")

    bid_list[name] = bid

    is_other_bidder = input("Are there any other bidders? Type 'yes' or 'no': ").strip().lower()

    if is_other_bidder not in ['yes', 'y']:
        break
    else:
        os.system('cls')

def find_best_bid(bids_dict):
    highest_bid = 0
    auction_winner = ""

    for bidder in list(bids_dict.keys()):
        if bids_dict[bidder] > highest_bid:
            highest_bid = bids_dict[bidder]
            auction_winner = bidder

    print(f"Auction winner is: {auction_winner} with a bid of £{highest_bid:.2f}")

find_best_bid(bid_list)
