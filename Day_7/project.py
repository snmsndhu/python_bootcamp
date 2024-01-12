#Hangman Project

import random
word_list = ["ardvark", "baboon", "camel"]
stages = ["Last chance", "5 chance", "4 chance", "3 chance", "2 chance"]

chosen_word = random.choice(word_list)
print(chosen_word)

display = []
total_lifes = 5

for _ in chosen_word:
    display += "_"
print(display)

end_game = False

while not end_game:
    guess = input("Guess your letter \n").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(display)

  
    # print(stages[1])
    # stages[1] += 1
    if total_lifes == 0:
        end_game = True
        print("you lost the game")
    elif not guess == chosen_word:
        total_lifes -= 1

    if "_" not in display:
        end_game = True
        print("you win")

    print(stages[total_lifes])