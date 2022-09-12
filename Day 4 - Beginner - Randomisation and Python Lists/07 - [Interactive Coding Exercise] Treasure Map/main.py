# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
maps = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

pstn = int(position)

if pstn == 11 or pstn == 21 or pstn == 31:
    if pstn == 11:
        row1[0] = "X"
    elif pstn == 21:
        row1[1] = "X"
    elif pstn == 31:
        row1[2] = "X"

elif pstn == 12 or pstn == 22 or pstn == 32:
    if pstn == 12:
        row2[0] = "X"
    elif pstn == 22:
        row2[1] = "X"
    elif pstn == 32:
        row2[2] = "X"

elif pstn == 13 or pstn == 23 or pstn == 33:
    if pstn == 13:
        row3[0] = "X"
    elif pstn == 23:
        row3[1] = "X"
    elif pstn == 33:
        row3[2] = "X"

else:
    print("Please type a valid number!")

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")