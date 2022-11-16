import pandas 

data = pandas.read_csv("D:/Python-Bootcamp/Day 25 - Intermediate - Working with CSV Data and the Pandas Library/02 - Reading CSV Data in Python/weather-data.csv")


# getting the data type
print(type(data))
print(type(data["temp"]))


# creating a dictionary
data_dict = data.to_dict()
print(data_dict)


# creating a list
temp_list = data["temp"].to_list()
print(temp_list)


# getting the avg of temp_list
total = 0
for i in data["temp"]:
    total += i
    
avg = total / len(data["temp"])
print(avg)