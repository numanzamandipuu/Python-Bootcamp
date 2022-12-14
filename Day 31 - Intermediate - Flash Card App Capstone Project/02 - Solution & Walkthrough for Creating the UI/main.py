from tkinter import *


FRONT = "D:/Python-Bootcamp/Day 31 - Intermediate - Flash Card App Capstone Project/02 - Solution & Walkthrough for Creating the UI/Images/card_front.png"
BACK = "D:/Python-Bootcamp/Day 31 - Intermediate - Flash Card App Capstone Project/02 - Solution & Walkthrough for Creating the UI/Images/card_back.png"
RIGHT = "D:/Python-Bootcamp/Day 31 - Intermediate - Flash Card App Capstone Project/02 - Solution & Walkthrough for Creating the UI/Images/right.png"
WRONG = "D:/Python-Bootcamp/Day 31 - Intermediate - Flash Card App Capstone Project/02 - Solution & Walkthrough for Creating the UI/Images/wrong.png"
DATA = "D:/Python-Bootcamp/Day 31 - Intermediate - Flash Card App Capstone Project/02 - Solution & Walkthrough for Creating the UI/Data/en_to_bn.csv"
BACKGROUND_COLOR = "#B1DDC6"


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx= 100, pady= 50, bg= BACKGROUND_COLOR)

front_img = PhotoImage(file= FRONT)
back_img = PhotoImage(file= BACK)
right_img = PhotoImage(file= RIGHT)
wrong_img = PhotoImage(file= WRONG)

canvas = Canvas(width= 450, height= 300, bg= BACKGROUND_COLOR, highlightthickness= 0)
canvas.create_image(225, 150, image= back_img)
canvas.create_text(225, 115, text= "Title", font= ("Ariel", 25, "italic"))
canvas.create_text(225, 175, text= "Word", font= ("Ariel", 40, "bold"))
canvas.grid(row= 1, column= 1, columnspan= 2)

right_button = Button(image= right_img, highlightthickness= 0)
right_button.grid(row= 2, column= 1)
wrong_button = Button(image= wrong_img, highlightthickness= 0)
wrong_button.grid(row= 2, column= 2)


window.mainloop()