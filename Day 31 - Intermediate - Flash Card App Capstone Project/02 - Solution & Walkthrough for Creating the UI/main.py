from tkinter import *


FRONT = "D:/Python-Bootcamp/Day 31 - Intermediate - Flash Card App Capstone Project/02 - Solution & Walkthrough for Creating the UI/card_front.png"
BACK = "D:/Python-Bootcamp/Day 31 - Intermediate - Flash Card App Capstone Project/02 - Solution & Walkthrough for Creating the UI/card_back.png"
RIGHT = "D:/Python-Bootcamp/Day 31 - Intermediate - Flash Card App Capstone Project/02 - Solution & Walkthrough for Creating the UI/right.png"
WRONG = "D:/Python-Bootcamp/Day 31 - Intermediate - Flash Card App Capstone Project/02 - Solution & Walkthrough for Creating the UI/wrong.png"


window = Tk()
window.title("Flashy")
window.config(padx= 100, pady= 50)



front_img = PhotoImage(file= FRONT)
back_img = PhotoImage(file= BACK)
right_img = PhotoImage(file= RIGHT)
wrong_img = PhotoImage(file= WRONG)


canvas = Canvas(width= 450, height= 300)
canvas.create_image(225, 150, image= back_img)
canvas.grid(row= 1, column= 1, columnspan= 2)

right_button = Button(image= right_img, highlightthickness= 0)
right_button.grid(row= 2, column= 1)
wrong_button = Button(image= wrong_img, highlightthickness= 0)
wrong_button.grid(row= 2, column= 2)




window.mainloop()