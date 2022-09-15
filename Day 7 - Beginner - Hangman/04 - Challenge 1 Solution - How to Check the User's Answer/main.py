#Step 1 
import random

word_list = ["ardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list)
word_list = list(chosen_word)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess_word = input("Guess a letter: ").lower()
guess = guess_word[0]

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for n in word_list:
    if guess == n:
        print("Right")
    else:
        print("Wrong")