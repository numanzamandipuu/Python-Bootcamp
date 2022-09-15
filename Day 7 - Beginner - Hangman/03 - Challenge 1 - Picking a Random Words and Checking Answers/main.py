import random

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
word_list = list(chosen_word)

guess_word = input("Guess a letter: ").lower()
guess = guess_word[0]

for n in word_list:
    if guess == n:
        print("Right")
    else:
        print("Wrong")