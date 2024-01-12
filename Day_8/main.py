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