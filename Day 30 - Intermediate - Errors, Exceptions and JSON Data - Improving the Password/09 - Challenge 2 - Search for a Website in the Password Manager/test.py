import json

with open("D:/Python-Bootcamp/Day 30 - Intermediate - Errors, Exceptions and JSON Data - Improving the Password/09 - Challenge 2 - Search for a Website in the Password Manager/data.json", "r") as file:
    data = json.load(file)

    for key in data:
        print(key)
        print(data[key]["email"])
        print(data[key]["password"])