import tkinter as tk

window = tk.Tk()
window.title("My First GUI Program")
window.minsize(width= 500, height= 300)


# Label

label = tk.Label(text= "I'm a Label", font= ("Ariel", 20))
label.pack()

label["text"] = "New Text"
label.config(text= "New Text")


# Button

def button_clicked():
    print("I got Clicked")
    new_text = text_input.get()
    label.config(text= new_text)

button = tk.Button(text= "Click Me", command= button_clicked)
button.pack()


# Entry

text_input = tk.Entry(width= 10)
text_input.pack()
text_input.get()


window.mainloop()