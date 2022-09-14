from replit import clear
from art import logo

print(logo)

new_bidder = True
while new_bidder:

    name = input("What is your name?: ")
    bid = input("What is your bid?: $")

    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.")
    if more_bidders == 'no':
        new_bidder = False
    clear()
