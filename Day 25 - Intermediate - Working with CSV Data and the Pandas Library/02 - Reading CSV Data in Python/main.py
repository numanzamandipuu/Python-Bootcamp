# with open("D:/Python-Bootcamp/Day 25 - Intermediate - Working with CSV Data and the Pandas Library/02 - Reading CSV Data in Python/weather-data.csv") as file:
#     data = file.readlines()
#     print(data)

# import csv

# with open("D:/Python-Bootcamp/Day 25 - Intermediate - Working with CSV Data and the Pandas Library/02 - Reading CSV Data in Python/weather-data.csv") as file:
#     data = csv.reader(file)
#     temperature = []

#     for i in data:
#         if i[1] == "temp":
#             pass
#         else:
#             temperature.append(int(i[1]))

#     print(temperature)


import pandas
