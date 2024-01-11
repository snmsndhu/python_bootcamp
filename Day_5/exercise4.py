#FizzBuzz Job interview question solution

target = int(input("write your number \n"))
for number in range(1, target + 1):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    
    else:
        print(number)