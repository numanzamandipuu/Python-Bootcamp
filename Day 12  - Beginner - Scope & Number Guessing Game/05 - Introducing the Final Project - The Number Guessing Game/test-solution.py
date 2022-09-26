import random
import art

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty_input = True
while difficulty_input == True:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        print("You have 10 attempts remaining to guess the number.")
        attempt = 10
        difficulty_input = False
    elif difficulty == "hard":
        print("You have 05 attempts remaining to guess the number.")
        attempt = 5
        difficulty_input = False
    else:
        print("Please choose a valid difficulty.")

number = random.randint(1, 100)

def attempt_left():
    print(f"You have {attempt} attempts remaining to guess the number.")

for n in range(0, attempt):
    guess = int(input("Make a guess: "))

    if attempt == 1 and guess != number:
        if guess > number: print("Too high.")
        elif guess < number: print("Too low.")
        print(f"You've run out of guesses, you lose. The currect number was {number}")
        break

    elif guess > number:
        print("Too high.\nGuess again.")
        attempt -= 1
        attempt_left()
    elif guess < number:
        print("Too low.\nGuess again.")
        attempt -= 1
        attempt_left()
    elif guess == number:
        print(f"You got it! The answer was {number}.")
        break