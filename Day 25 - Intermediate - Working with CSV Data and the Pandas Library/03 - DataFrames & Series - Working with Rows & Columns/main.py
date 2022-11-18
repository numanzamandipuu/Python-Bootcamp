import pandas 

data = pandas.read_csv("D:/Python-Bootcamp/Day 25 - Intermediate - Working with CSV Data and the Pandas Library/02 - Reading CSV Data in Python/weather-data.csv")


# # getting the data type
# print(type(data))
# print(type(data["temp"]))


# # creating a dictionary
# data_dict = data.to_dict()
# # print(data_dict)


# # creating a list
# temp_list = data["temp"].to_list()
# print(temp_list)

# print(data["temp"].mean())
# print(data["temp"].max())

# # get data in columns
# print(data["condition"])

# # get data in row
# print(data[data.temp == 14])
# print(data[data.temp == data.temp.max()])

# # creating a dataframe from scratch
data_dict = {
    "students" : ["amy", "james", "angela"],
    "score" : [1, 2, 3]
}
data = pandas.DataFrame(data_dict)
print(data)
# data.to_csv("D:/Python-Bootcamp/Day 25 - Intermediate - Working with CSV Data and the Pandas Library/02 - Reading CSV Data in Python/new-data.csv")