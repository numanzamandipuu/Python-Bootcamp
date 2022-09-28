import random
import game_data
import art
import os
clear = lambda: os.system("cls")

print(art.logo)
game_over = False
score = 0
list_of_index = list(range(0, len(game_data.data)))
compare_A_number = random.choice(list_of_index)

while game_over == False:

    compare_B_list = []
    for n in list_of_index:
        if n != compare_A_number:
            compare_B_list.append(n)
    compare_B_number = random.choice(compare_B_list)

    def compare_A(key):
        return game_data.data[compare_A_number][key]

    def compare_B(key):
        return game_data.data[compare_B_number][key]

    def comparison():
        if compare_A('follower_count') > compare_B('follower_count'):
            return "a"
        elif compare_A('follower_count') < compare_B('follower_count'):
            return "b"
    
    Compare_A = f"{compare_A('name')}, a {compare_A('description')}, from {compare_A('country')}."
    Compare_B = f"{compare_B('name')}, a {compare_B('description')}, from {compare_B('country')}."

    print(f"Compare A: {Compare_A}")
    print(art.vs)
    print(f"Against B: {Compare_B}")
    compare_input = input("Who has more followers? Type 'A' or 'B': ").lower()

    if comparison() == compare_input:
        score += 1
        clear()
        print(art.logo)
        print(f"You're right! Current score: {score}.")
        compare_A_number = compare_B_number

    elif comparison() != compare_input:
        clear()
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        game_over = True