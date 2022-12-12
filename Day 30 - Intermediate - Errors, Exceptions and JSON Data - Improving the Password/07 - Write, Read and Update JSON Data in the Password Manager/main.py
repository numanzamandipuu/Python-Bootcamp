import random
import pyperclip
from tkinter import *
from tkinter import messagebox
from random import shuffle
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    nr_letters= random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    random_letters = random.sample(letters, nr_letters)
    random_symbols = random.sample(symbols, nr_symbols)
    random_numbers = random.sample(numbers, nr_numbers)

    organized_password = random_letters + random_symbols + random_numbers
    shuffle(organized_password)

    password = "".join(organized_password)
    entry_03.delete(0, END)
    entry_03.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = entry_01.get()
    email = entry_02.get()
    password = entry_03.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title= "Oops!", message= "Please don't leave any fields empty!")

    else:
        with open("D:/Python-Bootcamp/Day 30 - Intermediate - Errors, Exceptions and JSON Data - Improving the Password/07 - Write, Read and Update JSON Data in the Password Manager/data.json", "w") as file:
            json.dump(new_data, file, indent= 4)
            entry_01.delete(0, END)
            entry_02.delete(0, END)
            entry_03.delete(0, END)
            entry_02.insert(0, "numanzamandipuu@gmail.com")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx= 50, pady= 50)

canvas = Canvas(height= 200, width= 200)
img_path = PhotoImage(file= "D:/Python-Bootcamp/Day 30 - Intermediate - Errors, Exceptions and JSON Data - Improving the Password/07 - Write, Read and Update JSON Data in the Password Manager/logo.png")
canvas.create_image(100, 100, image= img_path)
canvas.grid(row= 0, column= 1, sticky= "e")

label_01 = Label(text= "Website :")
label_01.config(padx= 5, pady= 5)
label_01.grid(row= 1, column= 0, sticky= "w")
label_02 = Label(text= "Email / Username :")
label_02.config(padx= 5, pady= 5)
label_02.grid(row= 2, column= 0, sticky= "w")
label_03 = Label(text= "Password :")
label_03.config(padx= 5, pady= 5)
label_03.grid(row= 3, column= 0, sticky= "w")

entry_01 = Entry(width= 70)
entry_01.focus()
entry_01.grid(row= 1, column= 1, columnspan= 2, sticky= "w")
entry_02 = Entry(width= 70)
entry_02.insert(0, "numanzamandipuu@gmail.com")
entry_02.grid(row= 2, column= 1, columnspan= 2, sticky= "w")
entry_03 = Entry(width= 38)
entry_03.grid(row= 3, column= 1, sticky= "w")

button_01 = Button(text= "Generate Password", width= 25, command= generate_password)
button_01.grid(row= 3, column= 2)
button_02 = Button(text= "Add", width= 59, command= save)
button_02.grid(row= 4, column= 1, columnspan= 2)


window.mainloop()