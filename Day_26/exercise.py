#Write a List comprehension to create a new list and make the each number from
#The old list squared.

number = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

square_list = [n * n for n in number]
print(square_list)