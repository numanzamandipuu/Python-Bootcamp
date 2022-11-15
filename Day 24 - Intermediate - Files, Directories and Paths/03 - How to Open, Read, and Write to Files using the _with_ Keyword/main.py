with open("D:/Python-Bootcamp/Day 24 - Intermediate - Files, Directories and Paths/03 - How to Open, Read, and Write to Files using the _with_ Keyword/main.txt") as file:
    content = file.read()
    print(content)

with open("D:/Python-Bootcamp/Day 24 - Intermediate - Files, Directories and Paths/03 - How to Open, Read, and Write to Files using the _with_ Keyword/new_file.txt", mode="w") as new_file:
    new_file.write("Hello Again.")