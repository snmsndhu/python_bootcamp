#How we can Tkinter to Create GUI(Graphical User Interfaces)

#Lets dive in

from tkinter import *

window = Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")

button = Button(text = "Click me")
button.pack()

window.mainloop()