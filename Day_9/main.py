#Dictionary and Nesting Lists

#syntax is like {"key": value}

dictionary = {
    "Bug": "error1",
    "Reason": "Thats why"
}

#Retrieving items from dictinoary.

print(dictionary["Bug"])

#Adding new items to dictionary

dictionary["Loop"] = "this is loop"
print(dictionary)


#Create an empty dictionary
empty_dic = {}

#Wipe an existing dictionary

dictionary = {}
print(dictionary)

#Edit an item in a dictionary

dictionary["Bug"] = "new value"
print(dictionary)

#Loop through a dictionary

for key in dictionary:
    print(key)
    print(dictionary[key])