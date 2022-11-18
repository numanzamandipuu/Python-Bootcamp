import pandas

data = pandas.read_csv("D:/Python-Bootcamp/Day 25 - Intermediate - Working with CSV Data and the Pandas Library/04 - The Great Squirrel Census Data Analysis (with Pandas!)/Squirrel-Data.csv")

Cinnamon = 0
Gray = 0
Black = 0

for color in data["Primary Fur Color"].tolist() :
    if color == "Cinnamon":
        Cinnamon += 1
    elif color == "Gray":
        Gray += 1
    elif color == "Black":
        Black += 1

color_dict = {
    "Fur Color" : ["gray", "red", "black"],
    "Count" : [Gray, Cinnamon, Black]
}

color_data = pandas.DataFrame(color_dict)
color_data.to_csv("D:/Python-Bootcamp/Day 25 - Intermediate - Working with CSV Data and the Pandas Library/04 - The Great Squirrel Census Data Analysis (with Pandas!)/Squirrel-Color-Data.csv")