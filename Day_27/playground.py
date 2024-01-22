#Lets create a function that can take unlimited positional arguments.

def add(*args):
    total = sum(args)
    print(total)

add(2,3,4,5,6)
