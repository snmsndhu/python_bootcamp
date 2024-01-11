#Write a function that calculate the sum of the all even numbers upto 100
#We are going to use the for loop with the range
target = int(input("write a number \n"))
sum = 0

for number in range(2, target + 1):
    if number % 2 == 0:
        sum += number

print(f"your total is {sum}")