import tkinter as tk

window = tk.Tk()
window.title("My First GUI Program")
window.minsize(width= 500, height= 300)
window.config(padx= 100, pady= 200)


# Label

label = tk.Label(text= "I'm a Label", font= ("Ariel", 20))
label.grid(row= 1, column= 1)
label.config(padx= 50, pady= 50)


# Button

def button_clicked():
    print("I got Clicked")
    new_text = text_input.get()
    label.config(text= new_text)

button = tk.Button(text= "Click Me", command= button_clicked)
button.grid(row= 2, column= 2)


# New Button

def button_clicked():
    print("I got Clicked")
    new_text = text_input.get()
    label.config(text= new_text)

button = tk.Button(text= "New Button", command= button_clicked)
button.grid(row= 1, column= 3)


# Entry

text_input = tk.Entry(width= 10)
text_input.grid(row= 3, column= 4)


window.mainloop()