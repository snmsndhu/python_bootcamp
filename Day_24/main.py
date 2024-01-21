#######  Working with local Files and Directories #######

"""
How can use Python to open the files and read from them and write in them.

We can use inbuild method to open up the file.

which is simple called open()

we can also open the file with word

with open("file_name") as file:

file here will the variable name.

To read from it we can use read()


Make sure at the last you close the file, by using the close() function.

"""


file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()