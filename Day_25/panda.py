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