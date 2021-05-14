#secret auction
import os
import secret_auction_art

#os.system('cls' if os.name == 'nt' else 'clear')
print(secret_auction_art.logo)
print("Welcome to the secret auction program")

bids = {}
bidding = True
while bidding:
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))

  bids[name] = bid #add bid to the dict

  more_bids = input("Are there any other bidders? Type 'yes' or 'no'\n")

  if more_bids == "no":
    bidding = False

  os.system('cls' if os.name == 'nt' else 'clear')

#find highest bidder
highest_bidder = ""
highest_bid = 0
for key in bids:
  if bids[key] > highest_bid:
    highest_bidder = key
    highest_bid = bids[key]

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")