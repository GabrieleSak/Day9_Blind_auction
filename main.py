from replit import clear
from art import logo

print(logo)

new_bidder = True
auction = {}
while new_bidder:

    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))

    auction[name] = bid

    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if more_bidders == 'yes':
        clear()
        print("clear()")
    else:
        new_bidder = False
        max_bid = 0
        for bidder in auction:
            if auction[bidder] > max_bid:
                max_bid = auction[bidder]
        print(f"The winner is {bidder} with a bid of ${max_bid}!")


