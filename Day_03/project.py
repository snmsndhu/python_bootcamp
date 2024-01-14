print("Welcome to Treasure Island. Your mission is to find the treasure")

answer = input("Where you would like to go 'left' or 'right' ")
if answer == "right":
    print("Game Over")
elif answer == "left":
    answer = input("would you swim or wait ")
    if answer == "swim":
        print("Game Over")
    elif answer == "wait":
        answer = input("Which door would you go Red, Blue, Yellow ")
        if(answer == "Red") or (answer == "Blue"):
            print("Game over")
        else:
            print("You win")