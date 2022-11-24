with open("D:/Python-Bootcamp/Day 26 - Intermediate - List Comprehension and the NATO Alphabet/05 - [Interactive Coding Exercise] Data Overlap/file1.txt") as file1:
    file1_list = file1.readlines()
    file1_list_2 = [int(n) for n in file1_list]
with open("D:/Python-Bootcamp/Day 26 - Intermediate - List Comprehension and the NATO Alphabet/05 - [Interactive Coding Exercise] Data Overlap/file2.txt") as file2:
    file2_list = file2.readlines()
    file2_list_2 = [int(n) for n in file2_list]

result = [n for n in file1_list_2 if n in file2_list_2]


# Write your code above 👆

print(result)