###### Creating Classes #######

#How we can create a class

#Syntax looks very simple

class User:
#Note word pass is used here to pass the Indent error, it is not a part of creating class.
    pass

#That all we need to create a class
#Now we will use our class to create a object.

user_1 = User()

#For the name a class we have to use the PascalCase
"""
So what is the PascalCase ?
First letter capital of the single word.

There are other two naming conventions.

camelCase
snake_case

it is same as the i wrote there names, that is the way to name them

in python camelCase is rarely used.
For everything else, rather then the CLASS, snake_case is used.
"""

#So next thing is how we can create Attributes in the class

##Attributes are basically a variable.
#Attributes are the things  that the object have.

"""
To do that we have to use the constructor.
So how can use the constructor?
let have a look in the example
"""
class Car:
    def __init__(self, seats):
        self.seats = seats

"""
This is how we can set attributes in the class, we can as many attributes we want after the self keyword.
when we will use the CLASS car to create a object we can pass those attributes and
it will be assigned to that attributes, that we have put in the CLASS
"""