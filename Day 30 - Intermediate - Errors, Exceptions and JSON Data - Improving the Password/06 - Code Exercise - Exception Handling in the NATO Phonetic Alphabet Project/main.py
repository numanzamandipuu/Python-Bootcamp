import pandas

data = pandas.read_csv("D:/Python-Bootcamp/Day 30 - Intermediate - Errors, Exceptions and JSON Data - Improving the Password/06 - Code Exercise - Exception Handling in the NATO Phonetic Alphabet Project/nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
output = True

while output:
    try:
        word = input("Enter a word: ").upper()
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        output = False

print(output_list)
