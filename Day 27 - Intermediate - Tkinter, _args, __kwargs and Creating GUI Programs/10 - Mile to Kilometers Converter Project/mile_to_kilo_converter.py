import tkinter as tk

window = tk.Tk()
window.title("Mile to Kilometer Converter")
window.minsize(height= 200, width= 400)
window.config(padx= 100, pady= 50)


def calculate():
    entry_value = int(entry.get())
    result = round(entry_value * 1.6)
    result_label.config(text= result)


# Entry
entry = tk.Entry()
entry.grid(row= 1, column= 2)


# Button
button = tk.Button(text= "Calculate", command= calculate)
button.grid(row= 3, column= 2)


# Label
label = tk.Label(text= "Miles")
label.grid(row= 1, column= 3)

label = tk.Label(text= "Kilometer")
label.grid(row= 2, column= 3)

label = tk.Label(text= "is equal to")
label.grid(row= 2, column= 1)

result_label = tk.Label()
result_label.grid(row= 2, column= 2)


window.mainloop()