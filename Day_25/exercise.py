## Printing the data from the CSV files

# with open("weather_data.csv") as data:
#     data_list = data.readlines()


# print(data_list)



"""
but here is problem in this approach, this will create little messy output with
quation.

we have a better apprach to read from the CSV files.

which is python build in CSV file. it will provide us a good formated list, which
we can loop through.

Lets have look.
"""


import csv

with open("weather_data.csv") as data:
    data_list = csv.reader(data)
    temperatures = []
    for row in  data_list:
        temp = row[1]
        temperatures.append(temp)
    print(temperatures)


