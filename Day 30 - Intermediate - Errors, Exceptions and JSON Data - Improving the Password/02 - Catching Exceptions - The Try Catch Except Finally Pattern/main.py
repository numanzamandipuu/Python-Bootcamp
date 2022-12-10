# FileNotFoundError
# with open("file.txt") as file:
#     file.read()

# KeyError
# a_dictionary = {"key" : "value"}
# value = a_dictionary["non_existing_key"]

# IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)

try:
    file = open("D:/Python-Bootcamp/Day 30 - Intermediate - Errors, Exceptions and JSON Data - Improving the Password/02 - Catching Exceptions - The Try Catch Except Finally Pattern/file.txt")
    a_dictionary = {"key" : "value"}
    print(a_dictionary["key"])

except FileNotFoundError:
    file = open("D:/Python-Bootcamp/Day 30 - Intermediate - Errors, Exceptions and JSON Data - Improving the Password/02 - Catching Exceptions - The Try Catch Except Finally Pattern/file.txt", "w")
    file.write("Something")

except KeyError as error_message:
    print(f"The key {error_message} does not exist")

else:
    content = file.read()
    print(content)

finally:
    file.close()
    print("File was closed.")