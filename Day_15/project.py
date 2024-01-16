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
        resources_check(drink["ingredients"])