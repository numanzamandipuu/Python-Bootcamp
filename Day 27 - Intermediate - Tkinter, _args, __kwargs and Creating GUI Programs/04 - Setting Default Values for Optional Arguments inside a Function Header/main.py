import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width= 500, height= 300)

label = tkinter.Label(text= "I'm a Label", font= ("Ariel", 20))
label.pack()


window.mainloop()