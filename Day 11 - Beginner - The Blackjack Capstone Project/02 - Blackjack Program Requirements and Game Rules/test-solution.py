import os
clear = lambda: os.system("cls")

start = True
while start:
    start_input = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if start_input == "y":
        start = False
    elif start_input == "n":
        start = False
    else:
        clear()
        print("Please pick a valid keyword.")