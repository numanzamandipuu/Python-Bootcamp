import pandas

file_path = "D:/Python-Bootcamp/Day 26 - Intermediate - List Comprehension and the NATO Alphabet/11 - Introducing the NATO Alphabet Project/nato_phonetic_alphabet.csv"
data = pandas.read_csv(file_path)

user_data = input("Enter a Word: ").upper()

dict_data = {
    row.letter :row.code for (index, row) in data.iterrows()
}

letter_list = [n for n in user_data]
new_list = [dict_data.get(n) for n in letter_list]

print(new_list)