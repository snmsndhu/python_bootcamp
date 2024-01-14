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

for key in operation:
    print(key)
should_continue = True
while should_continue:
    opt = input("What you want to do \n")
    num2 = int(input("What is the next number\n"))

    operation_chosen = operation[opt]

    result = operation_chosen(num1, num2)

    print(f"{num1} {opt} {num2} = {result}")

    if input(f"Type 'y' to continue or type 'n' to exit:\n") == "y":
        num1 = result
    else:
        should_continue = False
        print("Thanks for using the py cal")