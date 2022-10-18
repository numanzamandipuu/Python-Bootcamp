rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if choice < 0 or choice > 2:
    print("Please pick a valid number.")
else:
    if choice == 0:
        print(rock)
    elif choice == 1:
        print(paper)
    elif choice == 2:
        print(scissors)

    print("Computer chose:")
    number = random.randint(0 , 2)

    if number == 0:
        print(rock)
    elif number == 1:
        print(paper)
    elif number == 2:
        print(scissors)

    if choice == number:
        print("Match Drawn.")
    elif choice == 0 and number == 2:
        print("You Won!")
    elif choice == 0 and number == 1:
        print("You Lose!")
    elif choice == 1 and number == 0:
        print("You Won!")
    elif choice == 1 and number == 2:
        print("You Lose!")
    elif choice == 2 and number == 1:
        print("You Won!")
    elif choice == 2 and number == 0:
        print("You Lose!")