from tkinter import *
import math


# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#E2979C"
RED = "#E7305B"
GREEN = "#9BFEAC"
YELLOW = "#F7F5DD"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0


# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def timer_start():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 1:
        label.config(text= "Work", fg= GREEN)
        count_down(work_sec)

    elif reps % 8 == 0:
        label.config(text= "Break", fg= RED)
        count_down(long_break_sec)

    elif reps % 2 == 0:
        label.config(text= "Break", fg= PINK)
        count_down(short_break_sec)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text= f"{count_min}:{count_sec}")

    if count >= 0:
        window.after(1000, count_down, count - 1)

    elif count < 0:
        timer_start()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx= 80, pady= 50, bg= YELLOW)

label = Label(text= "Timer", font= (FONT_NAME, 35, "bold"), bg= YELLOW, fg= GREEN)
label.grid(column= 2, row= 1)

canvas = Canvas(width= 250, height= 270, bg= YELLOW, highlightthickness= 0)
tomato_img = PhotoImage(file= "D:/Python-Bootcamp/Day 28 - Intermediate - Tkinter, Dynamic Typing and the Pomodoro GUI Application/07 - Adding Checkmarks and Resetting the Application/tomato.png")
canvas.create_image(125, 130, image= tomato_img)
timer_text = canvas.create_text(125, 150, text= "00:00", fill= "white", font= (FONT_NAME, 35, "bold"))
canvas.grid(column= 2, row= 2)

button01 = Button(text= "Start", command= timer_start)
button01.grid(column= 1, row= 3)

button02 = Button(text= "Reset")
button02.grid(column= 3, row= 3)

tick_label = Label(text= "✔", bg= YELLOW, fg= GREEN, font= (FONT_NAME, 25, "bold"))
tick_label.grid(column= 2, row= 4)



window.mainloop()