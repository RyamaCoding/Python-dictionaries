import art
import os

print(art.logo)
print("Welcome to the secret auction")

name = input("What is your name?: \n")  
bid = int(input("What is your bid?: \n"))

bidder = [{
    "name": name,
    "price": bid, 
}]

next_bidder = input("Are there any other bidders? Type 'yes' or 'no'.\n")

while next_bidder == "yes":
    name = input("What is your name?: \n")
    bid = int(input("What is your bid?: \n"))

    empty_bidder = {}
    empty_bidder["name"] = name
    empty_bidder["price"] = bid
    bidder.append(empty_bidder)

    next_bidder = input("Are there any other bidders? Type 'yes' or 'no'.\n")

os.system('cls' if os.name == 'nt' else 'clear')

highest_bid = 0
highest_bidder = ""
for b in bidder:
    if b["price"] > highest_bid:
        highest_bid = b["price"]
        highest_bidder = b["name"]

print(f"The highest bidder is {highest_bidder} with a bid of ${highest_bid}")








