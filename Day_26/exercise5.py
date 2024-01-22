#Use the Dictionary Comprehension to create a new dictionary that has 
#fahrenheit insteed of degree.

#formula to convert the degree to fahrenheit => (temp_c * 9/5) + 32

dic_degree = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, 
              "Thursday": 14, "Friday": 21, 
              "Saturday": 22, "Sunday": 24}

dic_fahren = {day:(temp * 9/5) + 32 for (day, temp) in dic_degree.items() }

print(dic_fahren)