#Calculator App

print("Welcome to the py cal")

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operation = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}

num1 = int(input("What is the first number \n"))
num2 = int(input("What is the second number\n"))

for key in operation:
    print(key)

opt = input("What you want to do \n")

operation_chosen = operation[opt]

result = operation_chosen(num1, num2)

print(f"{num1} {opt} {num2} = {result}")