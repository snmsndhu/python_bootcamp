#BMI calculator with the if/else statement

# print("welcome to the BMI calculator")

# weight = int(input("What is your weight \n"))
# height = float(input("what is your height \n"))
# BMI = weight / (height ** 2)

# if BMI <= 18:
#     print(f"Your BMI is {BMI}, you are underweight")
# elif BMI <= 22:
#     print(f"Your BMI is {BMI}, you are normal weight")
# elif BMI <= 28:
#     print(f"Your BMI is {BMI}, you are slightly overweight")
# elif BMI <= 32:
#     print(f"Your BMI is {BMI}, you are obsese")
# else:
#     print(f"your BMI is above {BMI}, you are clinically obsese")


year = int(input("enter year"))

if year % 4 == 0:
 if year % 100 == 0:
  if year % 400 == 0:
   print("Leap year")
  else:
   print("Not a leap year")
 else:
  print("Leap year")
else:
 print("Not leap year")
