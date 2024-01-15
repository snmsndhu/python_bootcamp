#Number guessing Game
import random

easy_level_attempts = 10
hard_level_attempts = 5

def check_answer(guess, answer):
    if guess > answer:
        print("Too high")
    elif guess < answer:
        print("Too low")
    else:
        print(f"You got it The answer was {answer}")

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard'")
    if level == "easy":
        return easy_level_attempts
    else:
        return hard_level_attempts

print("Welcome to the number Guessing Game")
print("I'm thinking of a number between 1 and 100")

answer = random.randint(1, 100)

turns = set_difficulty()
print(f"You have {turns} attempts remaining to guess the number")
guess = int(input("Make a guess"))



