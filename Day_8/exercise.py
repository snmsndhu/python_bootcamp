#Function to calculate the cans for painting the wall

def can_calculator(height, width):
    number_of_cans = (height * width) / 5
    print(f"You will need {round(number_of_cans)} of cans")

can_calculator(2,4)