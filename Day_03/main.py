#Conditional Statements, Logical Operators, Code Blocks and Scope

# if/else Statement

print("Welcome to the rollercoaster")

height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
else:
    print("Sorry, you can't have a ride")


number = int(input("Write a number "))


if number % 2 == 0:
    print("This is the even number ")
else:
    print("This is the odd number ")


#Nested if/else statement
    
number = int(input("what is your height"))

if number >= 120:
    age = int(input("what is your age"))
    if age >= 10:
        print("you can take the ride")
    else:
        print("you can't take the ride")
else:
    print("you can't take the ride")

#elif condition
    
number = int(input("What is your age"))

if number <= 12:
    print("You have to pay $10")

elif number <=18:
    print("you have to pay $15")

else: 
    print("you have to pay $20")


#Logical Operators
    
#and => all the conditions has to be true to complete
#or => one condition has to be true to complete 
#not => it is oposite then the reguale condition statements