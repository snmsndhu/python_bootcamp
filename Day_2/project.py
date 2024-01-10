print("Welcome to the tip calculator")

total_bill = float(input("what was the total bill ? \n$" ))

tip_per = int(input("what percentage tip would you like to give ? 10, 12, or 15 \n"))

total_people = int(input("How many people to split the bill \n"))

total_tip = total_bill / 100 * tip_per

total_bill_with_tip = total_bill + total_tip

balance_for_each = round(total_bill_with_tip / total_people, 2)
balance = "{:.2f}".format(balance_for_each)

print(f"Each person is going to pay ${balance}")