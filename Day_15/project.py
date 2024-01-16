#Coffee Machine project

from coffee import MENU, resources
total_money = 0
on = True

def resources_check(order_ingre):
    for item in order_ingre:
        if order_ingre[item] >= resources[item]:
            print(f"There is not enough {item}")
            return False
    return True

def count_coins():
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many quarters?: ")) * 0.25
    total += int(input("How many quarters?: ")) * 0.25
    total += int(input("How many quarters?: ")) * 0.25
    return total




while on:
    choice = input("What would you like? (espresso/latte/cappuccino): \n")
    if choice == "off":
        on = False
    elif choice == "report":
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} ml")
        print(f"Money: ${total_money}")
    else:
        drink = MENU[choice]
        if resources_check(drink["ingredients"]):
            payment = count_coins()