#### List and Dictionary Comprehensions ####
"""
This is something which is very unique in the Python, and it will help
us to really cut down lot of code that we have to write when we are working,
with the List and Dictionary.

"""



####  List Comprehensions ####

"""

So, the big topic to explore is List Comprehension.
This is something very unique in Python.

So, what is List Comprehensions ?
This is way to create a new List from the previous List.

so how we will write our code?

new_list = [new_list for item in list_name]

its so easy to use it.

Suppose we have a list of number and we want to make a new list of numbers,
and in new list we want to add the 1 in each number.

number = [1,2,3]

so here is the way how we do it =>

new_list = [n + 1 for n in numbers]

This will give us 

new_list = [2,3,4]

It can also be used to other variable types. Like Strings

"""

"""
Conditonal List Comprehension

It allow us to add the test in the List comprehension method.

Here is the syntax for it.

new_list = [new_list for item in list_name if test]

we have to add the if test with the old syntax to create it.

"""

#In Python list, range, string, tuple they called sequences because they have
#specific order and when you perform a list comprehension, its going to take that
#sequence and it's goint to go through in order.