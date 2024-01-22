#How we can Tkinter to Create GUI(Graphical User Interfaces)

#Lets dive in

import tkinter

window = tkinter.Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()




window.mainloop()