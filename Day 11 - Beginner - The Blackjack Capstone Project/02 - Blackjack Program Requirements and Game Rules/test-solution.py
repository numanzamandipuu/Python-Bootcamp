import os
import random
clear = lambda: os.system("cls")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
my_card = random.sample(cards, 2)
sum_my_card = sum(my_card)

# print(f"Your cards: {my_card}, current score: {sum_my_card}")

computer_card = random.sample(cards, 2)
print(computer_card)
while sum(computer_card) < 17:
    add_computer_card = random.sample(cards, 1)
    if add_computer_card == [11] and sum(computer_card) > 10:
        add_computer_card = [1]
    computer_card.extend(add_computer_card)

print(computer_card)

# print(f"Computer's first card: {computer_card[0]}")
# yn_input = input("Type 'y' to get another card, type 'n' to pass: ")

# if yn_input == "y":
#     add_card = random.sample(cards, 1)
#     my_card.extend(add_card)
#     print(f"Your cards: {my_card}, current score: {sum_my_card}")

# start = True
# while start:
#     start_input = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
#     if start_input == "y":
#         start = False
#     elif start_input == "n":
#         start = False
#     else:
#         clear()
#         print("Please pick a valid keyword.")