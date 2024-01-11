#Build a Random name selector and name should be from the List

import random
names = ["X", "A", "B", "C", "D", "Y", "Z"]
num_items = len(names)

names_random = random.randint(0, num_items - 1)

result = names[names_random]

print(result)