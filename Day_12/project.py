#Number guessing Game
import random
print("Welcome to the number Guessing Game")
print("I'm thinking of a number between 1 and 100")

numbers_list = list(range(1, 101))
number_gussed = ""


number_to_guess = random.choice(numbers_list)

print(number_to_guess)
# def ran_number():


