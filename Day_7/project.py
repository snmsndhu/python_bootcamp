#Hangman Project

import random
word_list = ["ardvark", "baboon", "camel"]

chosen_world = random.choice(word_list)
print(chosen_world)

guess = input("Guess Your word \n").lower()


for world in chosen_world:
    if world == guess:
        print("Right")
    else:
        print("wrong")