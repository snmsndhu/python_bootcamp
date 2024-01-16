     ###### INTERMEDIATE LEVEL #########
###### Object Oriented Programming(OOP) #########

""" 
Object Oriented Programming is used to make the complex code easy to understand 
and easy to write.
All this is done by splitting all bif complez code in separate modules.
"""

##How we can implement the OOP##

#So an object is basically combining a some sort of Data and some sort of functionality
#Altogether in the same thing
"""
An object can generate multiple versions of the same object by using the blueprint.
In OOP we can this blueprint a CLASS.
and individual objects that are generated from that blueprint is called Object.

"""

##Lets make our object using the blueprint(CLASS)
##We are going a use a libaray called TURTLE

from turtle import Turtle, Screen
timmy = Turtle()

print(timmy)
timmy.shape("turtle")
timmy.color("red")
timmy.forward(90)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

##Python Packages

#Packages are different from the modules
##It is the whole bunch of code that is written by people and lots of file 
#all packaged togther to achieve some sort of goal or purpose
#Lets go to first exercise and have a look how it works
