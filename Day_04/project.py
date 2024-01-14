import random
print("Welcome")

game = ["ROCK", "PAPER", "SCISSORS"]
game_length = len(game)

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors. \n "))
if player >= 3 or player < 0 :
    print("You Lose")
else:
    print(f"you choose {game[player]}")


    computer = random.randint(1,2)
    print(f"computer choose {game[computer]}")



    if player == computer:
        print("Draw")

    elif player == 0 and computer == 1:
        print("You lose")
    elif player == 1 and computer == 2:
        print("You lose")
    elif player == 2 and computer == 0:
        print("You lose")
    else:
        print("You won")
    