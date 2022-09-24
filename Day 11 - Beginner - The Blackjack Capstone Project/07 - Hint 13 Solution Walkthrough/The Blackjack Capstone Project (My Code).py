import os
import random
import art
clear = lambda: os.system("cls")

def main_game():

    # Variables
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    my_card = random.sample(cards, 2)

    # Computer card
    computer_card = random.sample(cards, 2)
    while sum(computer_card) < 17:
        add_computer_card = random.sample(cards, 1)
        if add_computer_card == [11] and sum(computer_card) > 10:
            add_computer_card = [1]
        computer_card.extend(add_computer_card)
    computer_card_sum = sum(computer_card)

    # Functions
    def print_function():
        sum_my_card = sum(my_card)
        print(f"Your cards: {my_card}, current score: {sum_my_card}")
        print(f"Computer's first card: {computer_card[0]}")
    
    # Print and input
    print_function()
    yn_input = input("Type 'y' to get another card, type 'n' to pass: ")
    if yn_input == "y":
        looping = True
    elif yn_input == "n":
        looping = False
    else:
        print("Please pick a valid keyword.")
        looping = False

    # Main game using while
    while looping == True:
        add_card = random.sample(cards, 1)
        if add_card == [11] and sum(my_card) > 10:
            add_card = [1]
        my_card.extend(add_card)
        print_function()
        if sum(my_card) > 21:
            break
        yn_input = input("Type 'y' to get another card, type 'n' to pass: ")
        if yn_input == "y":
            looping = True
        elif yn_input == "n":
            looping = False
        else:
            print("Please pick a valid keyword.")
            looping = False

    # Result briefing
    print(f"Your final hand: {my_card}, final score: {sum(my_card)}")
    print(f"Computer's final hand: {computer_card}, final score: {computer_card_sum}")
    my_card_sum = sum(my_card)

    # Final result
    if my_card_sum > 21:
        print("You went over. You lose.")
    elif computer_card_sum > 21:
        print("Opponent went over. You win")
    elif my_card_sum == 21 and my_card_sum > computer_card_sum:
        print("Win with a Blackjack")
    elif computer_card_sum == 21 and my_card_sum < computer_card_sum:
        print("Lose with a Blackjack")
    elif my_card_sum < computer_card_sum:
        print("You lose.")
    elif my_card_sum > computer_card_sum:
        print("You win.")
    elif my_card_sum == computer_card_sum:
        print("Draw.")

# Game starts from here
start = True
while start:
    start_input = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if start_input == "y":
        clear()
        print(art.logo)
        main_game()
    elif start_input == "n":
        start = False
    else:
        clear()
        print("Please pick a valid keyword.")