#### Errors, Exceptions and Saving JSON Data ####

"""
Handling Erros & Exceptions
  So, how we can handle errors in the python, we have to make a error block,
  here is the code for it =>
  try:
  except:
  else:
  finally:
  
  we have to fill these.
  lets see how can make this working.
  In first line (try) we are executing some type of code.
  Second line (except) is the code that you want to be executed if there is exception.
  Third line (else) will executed if there is no errors in your (try).
  Fourth line (finally) will always going to be executed. Does not matter what happens in other 3 line of code.
"""

try: 
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist,")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed")