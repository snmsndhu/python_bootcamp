## Here we will try to use some Pandas methods.

import pandas

data = pandas.read_csv("weather_data.csv")

#we can convert the files in different type.

data_dictinoary = data.to_dict()
print(data_dictinoary)

# we can convert one single series to a differnt data or file type.
# Series is basically a coloum.

temp_list = data["temp"].to_list()

def average(list):
    aver = sum(list) / len(list)
    print(aver)

average(temp_list)

#We can also use the pandas methods to find the average.

print(data["temp"].mean())

#mean() is pandas method

#There are lot of other methods as well, check the pandas libary for it.

print(data["temp"].max())

#How to get to the coloums

print(data["condition"])

"""
That is the one way, but there is another way for doing it.
Behind the scenes panda converts all the coloums into the attributes.
so all we have to do is just get the same as we get the attributes.
"""


print(data.condition)