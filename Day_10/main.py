#Functions with Outputs

#To use the function with out we have to use the return statement

def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


#Then we can store the function in another variable and simply use it

print(format_name("john", "jatt"))