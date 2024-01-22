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

#Unlimited Positional Arguments

"""
So, how we can make our function to take unlimited numbers of positional arguments?
This is pretty easy all we have to do is pass the * before the argument name in the arguments and it will take unlimited 
number of positional arguments.
This is how it will look like =>
def add(*args):
   for n in args:
   print(n)

This is basically a tuple that we are passing, asterix(*) collects all of the arguments into a tuple.
By this we can provide as many values we want to provide to one arguments.
   
This function will take as many positional arguments you can provide.
"""

#Unlimited Keyword Arguments

"""
In this we can provide as many arguments to the function without defining them, in the function when we are creating it.

Basically its syntax will look like this =>

def calculate(**kwargs):
    print(kwargs)

All we have to do is add double ** to the function and then just pass in the name which is kwargs used by most of developers,
but it could be anything, totally depends on the developer.

After defining the function when we are calling it, we can provide as many keyword arguments in the function.
calculate(add = 3, multi = 5)

"""