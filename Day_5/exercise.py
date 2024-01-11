#Average height exercise
#It has to be done by using the for loop, len() and the sum() function can't be used.

students = [180, 124, 165, 173, 189, 169, 146]\

total_students = 0

for student in students:
    total_students += 1

total_height = 0

for student in students:
    total_height += student

average_height = total_height / total_students

print(round(average_height, 2))