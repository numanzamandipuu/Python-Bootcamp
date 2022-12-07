from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx= 20, pady= 20)

canvas = Canvas(height= 200, width= 200)
img_path = PhotoImage(file= "D:/Python-Bootcamp/Day 29 - Intermediate - Building a Password Manager GUI App with Tkinter/02 - Challenge 1 - Working with Images and Setting up the Canvas/logo.png")
canvas.create_image(100, 100, image= img_path)
canvas.pack()


window.mainloop()