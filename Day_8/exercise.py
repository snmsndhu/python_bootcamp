#Function to calculate the cans for painting the wall
import math

def can_calculator(height, width):
    number_of_cans = (height * width) / 5
    print(f"You will need {math.ceil(number_of_cans)} of cans")

can_calculator(3,9)