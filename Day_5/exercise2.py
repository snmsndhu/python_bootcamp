#High score exercise

student_score = [78, 65, 89, 86, 55, 91, 64, 89]

high_score = 0

for score in student_score:
    if score > high_score:
        high_score = score
        
print(high_score)