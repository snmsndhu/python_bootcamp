"""
Write a List Comprehension to create a new list that has common numbers from two 
different files, those files are containing the numbers only.
"""

with open("file1.txt") as first_list:
    first_content = first_list.readlines()

with open("file2.txt") as second_list:
    second_content = second_list.readlines()
    

result = [int(num) for num in first_content if num in second_content]

print(result)