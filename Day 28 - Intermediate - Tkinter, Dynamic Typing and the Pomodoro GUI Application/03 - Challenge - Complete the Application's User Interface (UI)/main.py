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
window.config(padx= 80, pady= 50, bg= YELLOW)

label = Label(text= "Timer", font= (FONT_NAME, 35, "bold"), bg= YELLOW, highlightthickness= 0, fg= GREEN)
label.grid(column= 2, row= 1)

canvas = Canvas(width= 250, height= 270, bg= YELLOW, highlightthickness= 0)
tomato_img = PhotoImage(file= "D:/Python-Bootcamp/Day 28 - Intermediate - Tkinter, Dynamic Typing and the Pomodoro GUI Application/03 - Challenge - Complete the Application's User Interface (UI)/tomato.png")
canvas.create_image(125, 130, image= tomato_img)
canvas.create_text(125, 150, text= "00:00", fill= "white", font= (FONT_NAME, 35, "bold"))
canvas.grid(column= 2, row= 2)

button01 = Button(text= "Start")
button01.grid(column= 1, row= 3)

button02 = Button(text= "Reset")
button02.grid(column= 3, row= 3)

tick_label = Label(text= "✔", bg= YELLOW, fg= GREEN, font= (FONT_NAME, 25, "bold"))
tick_label.grid(column= 2, row= 4)



window.mainloop()