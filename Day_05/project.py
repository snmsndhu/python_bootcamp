#Final project of the day
#PyPassword Generator

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']


print("Welcome to the PyPassword Generator!")


total_letters = int(input("How many letters would you like in your password? \n"))
total_numbers = int(input("How many numbers would you like in your password? \n"))
total_symbols = int(input("How many symbols would you like in your password? \n"))

password = []
for letter in range(1, total_letters + 1):
    password += random.choice(letters)

for letter in range(1, total_numbers + 1):
    password += random.choice(numbers)

for letter in range(1, total_symbols + 1):
    password += random.choice(symbols)

random.shuffle(password)

result = ""
for char in password:
    result += char

print(f"Your password is: {result}")