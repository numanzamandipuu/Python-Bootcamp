import random
import game_data
import art

# print(game_data.data[10]['description'])

# print(art.logo)

# Comparison number detection
compare_A_number = random.choice(list(range(0, len(game_data.data))))
compare_B_whole_number = list(range(0, len(game_data.data)))
compare_B_whole_number.remove(compare_A_number)
compare_B_number = random.choice(compare_B_whole_number)

# All the functions
def compare_A(key):
    return game_data.data[compare_A_number][key]
def compare_B(key):
    return game_data.data[compare_B_number][key]

def comparison():
    if compare_A('follower_count') > compare_B('follower_count'):
        return "a"
    elif compare_A('follower_count') < compare_B('follower_count'):
        return "b"

print(f"Compare A: {compare_A('name')}, a {compare_A('description')}, from {compare_A('country')}.")
print(f"Compare B: {compare_B('name')}, a {compare_B('description')}, from {compare_B('country')}.")

compare_input = input("Who has more followers? Type 'A' or 'B': ").lower()

if comparison() == compare_input:
    print("right madafaka")
elif comparison() != compare_input:
    print("you fuckin donkey")