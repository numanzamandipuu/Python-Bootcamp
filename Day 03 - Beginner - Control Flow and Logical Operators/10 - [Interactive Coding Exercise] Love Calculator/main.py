# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1_lower = name1.lower()
name2_lower = name2.lower()

name1_t = name1_lower.count("t")
name2_t = name2_lower.count("t")
name1_r = name1_lower.count("r")
name2_r = name2_lower.count("r")
name1_u = name1_lower.count("u")
name2_u = name2_lower.count("u")
name1_e = name1_lower.count("e")
name2_e = name2_lower.count("e")
name1_l = name1_lower.count("l")
name2_l = name2_lower.count("l")
name1_o = name1_lower.count("o")
name2_o = name2_lower.count("o")
name1_v = name1_lower.count("v")
name2_v = name2_lower.count("v")

true = name1_t + name2_t + name1_r + name2_r + name1_u + name2_u + name1_e + name2_e 
love = name1_l + name2_l + name1_o + name2_o + name1_v + name2_v + name1_e + name2_e

string_true = str(true)
string_love = str(love)

true_love = int(string_true + string_love)

if true_love < 10 or true_love > 90:
    print(f"Your score is {true_love}, you go together like coke and mentos.")
elif true_love >= 40 and true_love <= 50:
    print(f"Your score is {true_love}, you are alright together.")
else:
    print(f"Your score is {true_love}.")