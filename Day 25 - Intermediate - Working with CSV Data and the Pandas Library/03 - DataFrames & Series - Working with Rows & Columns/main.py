import pandas 

data = pandas.read_csv("D:/Python-Bootcamp/Day 25 - Intermediate - Working with CSV Data and the Pandas Library/02 - Reading CSV Data in Python/weather-data.csv")

print(type(data))
print(type(data["temp"]))

data_dict = data.to_dict()
print(data_dict)