#Creating a Body Mass calculator

height = input("what is your height ")
new_height = float(height)
weight = input("what is your weight ")
new_weight = float(weight)

BMI = new_weight / (new_height ** 2)

Result = round(BMI, 2)

print(Result)