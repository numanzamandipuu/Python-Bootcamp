from tkinter import *
import pandas as pd
import random


FRONT = "D:/Python-Bootcamp/Day 31 - Intermediate - Flash Card App Capstone Project/05 - Solution & Walkthrough for Saving Progress/Images/card_front.png"
BACK = "D:/Python-Bootcamp/Day 31 - Intermediate - Flash Card App Capstone Project/05 - Solution & Walkthrough for Saving Progress/Images/card_back.png"
RIGHT = "D:/Python-Bootcamp/Day 31 - Intermediate - Flash Card App Capstone Project/05 - Solution & Walkthrough for Saving Progress/Images/right.png"
WRONG = "D:/Python-Bootcamp/Day 31 - Intermediate - Flash Card App Capstone Project/05 - Solution & Walkthrough for Saving Progress/Images/wrong.png"
DATA = "D:/Python-Bootcamp/Day 31 - Intermediate - Flash Card App Capstone Project/05 - Solution & Walkthrough for Saving Progress/Data/en_to_bn.csv"
BACKGROUND_COLOR = "#B1DDC6"
card = {}


# ---------------------------- NEW FLASH CARD ------------------------------- #

dataframe = pd.read_csv(DATA)
data = dataframe.to_dict(orient= "records")

def flash_card():
    global card, loop
    window.after_cancel(loop)
    index = random.randint(0, 499)
    card = data[index]
    canvas.itemconfig(word_text, text= card["ENGLISH"], fill= "white")
    canvas.itemconfig(title_text, text= "English", fill= "white")
    canvas.itemconfig(card_img, image= back_img)
    loop = window.after(3000, flip_card)


# ---------------------------- FLIP THE CARD ------------------------------- #

def flip_card():
    global card
    canvas.itemconfig(word_text, text= card["BANGLA"], fill= "black")
    canvas.itemconfig(title_text, text= "Bangla", fill= "black")
    canvas.itemconfig(card_img, image= front_img)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx= 100, pady= 50, bg= BACKGROUND_COLOR)

front_img = PhotoImage(file= FRONT)
back_img = PhotoImage(file= BACK)
right_img = PhotoImage(file= RIGHT)
wrong_img = PhotoImage(file= WRONG)

canvas = Canvas(width= 450, height= 300, bg= BACKGROUND_COLOR, highlightthickness= 0)
card_img = canvas.create_image(225, 150, image= back_img)
title_text = canvas.create_text(225, 115, text= "", font= ("Ariel", 25, "italic"))
word_text = canvas.create_text(225, 175, text= "", font= ("Ariel", 40, "bold"))
canvas.grid(row= 1, column= 1, columnspan= 2)

right_button = Button(image= right_img, highlightthickness= 0, command= flash_card)
right_button.grid(row= 2, column= 1)
wrong_button = Button(image= wrong_img, highlightthickness= 0, command= flash_card)
wrong_button.grid(row= 2, column= 2)

loop = window.after(3000, flip_card)
flash_card()


window.mainloop()