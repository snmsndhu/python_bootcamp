#Namespaces
#Local vs Global Scope


########## SCOPE ##########

#Local Scope

#Local Scope exist within the Functions
#We can have a access of it outside of the function
 
#let see a example of local scope

def print_amount():
    amount = 2
    print(amount)

#Now if we call that function we will get the value of 2 because we print that 
#variable inside the function

#But if i try to print that variable outside of the function it will not work
print_amount()  

# print(amount)
#It will show me error of amount undefined

#Global Scope

#Major difference between the local scope and the global scope is that
#Where you define the variable
#It will effect the availbility and functionality of the variable
#Global Scope variable will be defined Globally, which means outside of everything
#And it can be used inside the function the functions and in other ways as well

#Lets have a example of Global Scope

player_health = 10

def drink_potion():
    print(player_health)

drink_potion()

#It will print that global variable

############ NameSpace #############

#Anything that you give a name to has a namespace and that namespace is valid in
#certain scopes
#That mean local or global scopes are not only for the variables
#That effects everything that we give a name
#Example, if we define a function inside a funcion that function will be only accesiable 
#with outside defined function


"""
Another point to notice is that if the varibale is defined in the loop
or inside the if statement it has the global scope
 """

#So how to Modify a Global variable

enemies = 1

def increase_enemies():
    global enemies
    enemies += 1
    print(enemies)

increase_enemies()

### It is highly suggest that do not modifie a global variable in the function
## So how can do it in right way

#Lets have a look

def increase_enemies_return():
    return enemies + 4

enemies = increase_enemies_return()
print(f"return statement {enemies}")


#### Global Constants #####

#Global constants are something that you never wanted to change at any time

#Naming convention in python for the Global Constants is all upper case 