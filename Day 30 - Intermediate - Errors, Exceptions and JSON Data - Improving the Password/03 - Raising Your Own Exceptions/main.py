# try:
#     file = open("D:/Python-Bootcamp/Day 30 - Intermediate - Errors, Exceptions and JSON Data - Improving the Password/02 - Catching Exceptions - The Try Catch Except Finally Pattern/file.txt")
#     a_dictionary = {"key" : "value"}
#     print(a_dictionary["key"])

# except FileNotFoundError:
#     file = open("D:/Python-Bootcamp/Day 30 - Intermediate - Errors, Exceptions and JSON Data - Improving the Password/02 - Catching Exceptions - The Try Catch Except Finally Pattern/file.txt", "w")
#     file.write("Something")

# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")

# else:
#     content = file.read()
#     print(content)

# finally:
#     raise TypeError("This is an error I made up.")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)