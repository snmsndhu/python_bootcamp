#Write a Function to check if the number is prime number or not

def prime_check(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It is Prime Number")
    else:
        print("It is not a prime number")

prime_check(4)