#Now we see how we can loop the panda frame.

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through dictionaries:

for (key, value) in student_dict.items():
    print(value)

#Lets see how to do with panda
    
import pandas

student_data_frame = pandas.DataFrame(student_dict)

for(key, value) in student_data_frame.items():
    print(key)