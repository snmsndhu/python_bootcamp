#IndexError Handing

fruits = ["Apple", "Pear", "Orange"]
def make_pie(index):
    fruit = fruits[index]
    print(fruit + "pie")

try:
    make_pie(index=2)

except:
    print("Fruit pie")