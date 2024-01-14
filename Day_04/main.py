#Randomisation and Python Lists

#How to generate the random number

import random

random_int = random.randint(1,100)

print(random_int)

#How to generate the floating random number

float_random = random.random()

print(float_random)

random_float = random.random() * 5

print(random_float)

#Lists

english_alphabetes = ["A", "B", "C"]

print(english_alphabetes[1])

#Nested Lists

names = ["X", "A", "B", "C", "D", "Y", "Z"]

english_alphabetes = ["A", "B", "C"]

nested_list = [names, english_alphabetes]

print(f"nested list {nested_list[1][1]}")