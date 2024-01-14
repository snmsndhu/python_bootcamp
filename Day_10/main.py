#Functions with Outputs

#To use the function with out we have to use the return statement

def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


#Then we can store the function in another variable and simply use it

print(format_name("john", "jatt"))

#What will happen with more then 1 return statement

#We can have multiple return statements 
#Whatever condition matches first and if it has the return statement
#it will terminate the fucntion over there

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didnt provide the names"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


print(format_name("", ""))

#Docstrings

#This could be used to add multiline string and it can help to make documentation of any function 
#or any other documentation in the app

#all should be done to use it, is use """ """ and your doc inside it

"""
here we can type anthing and it will allow us use multiple
line in it
"""
