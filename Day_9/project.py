#BID Taker Project


print("Welcome to the BID Taker")



bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

while not bidding_finished:
    name = input("What is your name\n$")
    price = int(input("How much you want to bid\n"))
    bids[name] = price
    other_user = input("If there is other users who want to Bid. Type 'yes' or 'no'\n")
    if other_user == "no":
        bidding_finished = True
    elif other_user =="yes":
        print("clear")
