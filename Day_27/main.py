### Graphical User Interfaces with Tkinter and Function Arguments ###

#We will also look on some advanced features of the python
## Default Arguments , Args, Kwargs.
#How we can Tkinter to Create GUI(Graphical User Interfaces)

#Lets dive in

import tkinter

window = tkinter.Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()




window.mainloop()


#Advanced Arguments

"""
Lets talk about Advance arguments bit more, in order to specify wider range of input.
We know how keyword arguments works.
In python we can create arguments that have default values. we can do this by simple giving default
values to the arguments, when we define a function. When we call this function, we dont need to provide any
values to the arguments.
But if we want to give a custom value to any of the argument, we can simply do that by giving it,
when we are calling the function.

"""

#Unlimited Arguments

"""
So, how we can make our function to take unlimited numbers of arguments?
This is pretty easy all we have to do is pass the *args in the arguments and it will take unlimited 
number of arguments.
This is how it will look like =>
def add(*args):
   for n in args:
   print(n)

   
This function will take as many arguments you can provide.
"""