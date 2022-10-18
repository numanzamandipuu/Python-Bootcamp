import os
import art
clear = lambda: os.system("cls")

print(art.logo)
auction = {}
stop_auction = False
question = "yes"

while stop_auction == False:
    if question == "yes":
        key = input("What is your name?: ")
        value = int(input("What is your bid?: $"))
        auction[key] = value
        question = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
        if question == "yes":
            clear()     
    elif question == "no":
        stop_auction = True
    else:
        print("You've picked an invalid keyword.\nEnd of the auction.")
        stop_auction = True

winner = max(auction, key=auction.get)
amount = auction[winner]

print(f"The winner is {winner} with a bid of ${amount}")