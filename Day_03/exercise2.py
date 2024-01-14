#Building a simple pizza making app

print("Thank you for choosing Python Pizza Deliveries! \n")
size = input("What size pizza do you want? S, M, or L \n")
add_pepperoni = input("Do you want pepperoni? Y or N \n")
extra_cheese = input("Do you want extra cheese? Y or N \n")

bill = 0

if size == "S":
 bill = 15
 print("Price for the small pizza is $15")
 if add_pepperoni == "Y":
  bill += 2
  print("There is $2 charge for the adding pepperoni for the small pizza")
elif size == "M":
 bill = 20
 print("Price for the Medium pizza is $20")
elif size == "L":
 bill = 25
 print("Price for the Large pizza is $25")
 if add_pepperoni =="Y":
  bill += 3
  print("There is $3 charge for the adding pepperoni for the medium and large pizza")
if extra_cheese == "Y":
 bill += 1
 print("There is $1 charge for the adding extra cheese for the all pizzas")

 print(f"Your total bill for the order is ${bill}")

 