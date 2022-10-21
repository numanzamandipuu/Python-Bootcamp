# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

import random

length = len(names)
number = random.randint(0 , length - 1)
final_name = names[number]

print(f"{final_name} is going to buy the meal today!")