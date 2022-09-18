import os
import art
clear = lambda: os.system("cls")

print(art.logo)
auction = {}
stop_auction = False

key = input("What is your name?: ")
value = int(input("What is your bid?: $"))
auction[key] = value
question = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()

while stop_auction == False:
    if question == "yes":
        clear()
        key = input("What is your name?: ")
        value = int(input("What is your bid?: $"))
        auction[key] = value
        question = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    elif question == "no":
        stop_auction = True
    else:
        print("You've picked an invalid keyword.\nEnd of the auction.")
        stop_auction = True

print(auction)