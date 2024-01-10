#Converting a Interger into a string

string = len(input("what is your name"))
new_string = str(string)
print("Your name has " + new_string + " char")


#Converting a string into a interger

number = 35

new_number = str(number)

print(int(new_number[0]) + int(new_number[1]))


#Mathematical Operations

print(3 + 5)
print(7 - 4)
print(3 * 2)
print(6 / 2)
print(2 ** 6)

#PEMDAS

#Parentheses ()
#Exponents **
#Multiplication *
#Division /
#Addition +
#Subtraction -

# How to print different type of data types without changing them ?
# We can use the f-string

score = 0
heigth = 1.8
isWinning = True

#f-string
print(f"your score is {score}, your height is {heigth}, you are winnig is {isWinning}")