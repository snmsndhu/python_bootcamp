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


#Nesting a List in a Dictionary 
#Nesting Dictionary in a Dictionary
    
travel_log = {
    "France": {"cities_visited":["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}



