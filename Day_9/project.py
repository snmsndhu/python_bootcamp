#BID Taker Project


print("Welcome to the BID Taker")

name = input("What is your name\n")

bid = int(input("How much you want to bid\n"))

biders = []

def bid_taker(bider_name, bider_amount):
    new_bid = {}
    new_bid["name"] = bider_name
    new_bid["bid"] = bider_amount
    biders.append(new_bid)

    other_user = input("If there is other users who want to Bid. Type 'Yes' or 'No'\n")

    if other_user == "Yes":
        print()
        


        
    

    

bid_taker(name, bid)
print(biders)