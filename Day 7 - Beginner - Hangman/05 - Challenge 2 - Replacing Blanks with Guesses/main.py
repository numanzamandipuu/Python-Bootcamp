import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

print(f'Pssst, the solution is {chosen_word}.')
guess = input("Guess a letter: ").lower()

display = []
for alphabet in chosen_word:
    display == display.append("_")

for n in range(word_length):
    if guess == chosen_word[n]:
        display[n] = guess

print(display)