#Write a List Comprehension to make a new list of old list that have only even numbers


numbers = [9, 0, 32, 8, 2, 8, 64, 29, 42, 99]

even_numbers = [num for num in numbers if num % 2 == 0]

print(even_numbers)