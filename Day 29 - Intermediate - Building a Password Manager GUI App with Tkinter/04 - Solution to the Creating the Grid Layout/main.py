from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx= 50, pady= 50)

canvas = Canvas(height= 200, width= 200)
img_path = PhotoImage(file= "D:/Python-Bootcamp/Day 29 - Intermediate - Building a Password Manager GUI App with Tkinter/04 - Solution to the Creating the Grid Layout/logo.png")
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
entry_01.grid(row= 1, column= 1, columnspan= 2, sticky= "w")
entry_02 = Entry(width= 70)
entry_02.grid(row= 2, column= 1, columnspan= 2, sticky= "w")
entry_03 = Entry(width= 38)
entry_03.grid(row= 3, column= 1, sticky= "w")

button_01 = Button(text= "Generate Password", width= 25)
button_01.grid(row= 3, column= 2)
button_02 = Button(text= "Add", width= 59)
button_02.grid(row= 4, column= 1, columnspan= 2)


window.mainloop()