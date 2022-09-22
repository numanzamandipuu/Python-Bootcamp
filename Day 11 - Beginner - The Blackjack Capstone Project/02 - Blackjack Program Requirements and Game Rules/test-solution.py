import os
import random
clear = lambda: os.system("cls")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
my_card = random.sample(cards, 2)
sum_my_card = sum(my_card)

print(f"Your cards: {my_card}, current score: {sum_my_card}")

computer_card = random.sample(cards, 2)
print(f"Computer's first card: {computer_card[0]}")
print(computer_card)



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