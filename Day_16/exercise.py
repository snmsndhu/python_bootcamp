##Python Packages

from prettytable import PrettyTable


table = PrettyTable()

table.field_names = ["Pokmon Name", "Type"]
table.add_row([
    ["Pikachu", "Electric"],
    ["Squirtle", "Water"],
    ["Charmander", "Fire"]
])
print(table)