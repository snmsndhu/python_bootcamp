import pandas


data = pandas.read_csv("squirrel_data.csv")
grey_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels, red_squirrels, black_squirrels]
}


df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")