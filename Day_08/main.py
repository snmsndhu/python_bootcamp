#Functions with Inputs

def greet():
    name = input("what is your name \n")
    print(f"Hello {name}")
    print("How are you")

greet()


#Arguments & Parameters

#So how this function is working 
#it is taking an parameter in the function and when we are calling this function we are passing an argument 
#in the space of Parameter

def greet_with_argument(name):
    print(f"Hello {name}")
    print("How are you")

greet_with_argument("j")

#Function with more than 1 input

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"Your address is {location}")

greet_with("j", "124")

#Function with keyword arguments

def great_with(name, address):
    print(f"Hello {name}")
    print(f"Your address is {address}")


great_with(name = "j", address= "1234")