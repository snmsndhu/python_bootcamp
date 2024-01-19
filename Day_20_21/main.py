#######  Building the Snake Game #########


#Steps to make the game


#1 Creating a snake body.
#2 Move the snake.
#3 Create snake food.
#4 Delect collision with food.
#5 Create a scoreboard.
#6 Detect collision with wall.
#7 Detect collision with tail.



"""
In building this game we will cover a new topic which is CLASS inheritance,
which means CLASS can inherit from another classes, which will improve 
our OOP knowledge.
We can inherit our Class methods in the new Class.

How the syntax will look like =>

class Fish(Animal):
    def __init__(self):
       super().__init__()

Over here we are inherting from the Class Animal in the Fish Class.
and we have to add super().__init__() inside the Class to inherit all the attribute
and the methods of the Animal Class in the Fish Class.

The call to super() in the initialiser is recommended, but not strictly required.
"""

#We will also cover the SLICING.

"""
If we want to hold a small section of the list, we can use the Slice to slice the
list and use it latter on.
so how we can implement it =>

suppose we have list of the piano keys and we want to slice some part of it.
syntax will be =>

piano_keys[2:5]

so we have one another very useful trick to make to which is called Neat Trick.

so what it does in slicing ?

piano_keys(::-1)

it will reverse the list for us.
It is very help full in solving different type of coding problems.
This method also works with tuple.
"""