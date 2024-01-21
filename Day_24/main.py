#######  Working with local Files and Directories #######

"""
How can use Python to open the files and read from them and write in them.

We can use inbuild method to open up the file.

which is simple called open()


To read from it we can use read()


Make sure at the last you close the file, by using the close() function.

"""


file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()

"""
Lets try with different method to open the file and in this method we do not
need to close the file at the end.

with open("file_name") as file:

file here will the variable name.
"""

with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

"""
Lets see how we can write in the file
after opening the file with (with keyword) we have to mention the method in the 
open function, that we want to write in this file.
Lets have a look in the syntax.

With the "w" mode we can also create a new file, ex. if the name that we have mentioned in the 
open function and that file does not exist, its going to create that file and write the text 
that you have mentioned in the write function.
"""

with open("my_file.txt", mode = "w") as file:
    file.write("New Text.")

"""
This will delete everything in the file and add the new text, that we will pass in it.
    
But if you want to edit the text, instead to delete the old text, all we have to do is just put "a" in
the method instead of the "w".
"""

with open("my_file.txt", mode = "a") as file:
    file.write("New Text.")


#### File Path #####
    
"""
so how  we have reach a file, that is in different folder?

Absolute File Path
That file path starts from the top the folder directory.

Relative File Path
Its start from the folder that you are in andn trying to access to file and same folder.

so how we can go in the folder in both Paths.
/folder1/folder2/file.py

so how we go outside the folder to select the file that is in other folder.

we can use ../folder1/

that we put us one folder up, if we want to go up two folders,
we can simply use 
../../folder1
"""