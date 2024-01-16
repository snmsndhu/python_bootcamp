#Coffee Machine project

from coffee import MENU, resources

on = True

while on:
    choice = input("What would you like? (espresso/latte/cappuccino): \n")
    if choice == "off":
        on = False