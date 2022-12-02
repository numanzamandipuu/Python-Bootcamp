from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#E2979C"
RED = "#E7305B"
GREEN = "#9BFEAC"
YELLOW = "#F7F5DD"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx= 80, pady= 40, bg= YELLOW)

canvas = Canvas(width= 250, height= 270, bg= YELLOW, highlightthickness= 0)
tomato_img = PhotoImage(file= "D:/Python-Bootcamp/Day 28 - Intermediate - Tkinter, Dynamic Typing and the Pomodoro GUI Application/02 - How to work with the Canvas Widget and Add Images to Tkinter/tomato.png")
canvas.create_image(125, 130, image= tomato_img)
canvas.create_text(125, 150, text= "00:00", fill= "white", font= (FONT_NAME, 35, "bold"))

canvas.pack()



window.mainloop()