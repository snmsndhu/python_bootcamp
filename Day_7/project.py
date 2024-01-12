#Hangman Project

import random
word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

guess = input("Guess your letter \n").lower()


for world in chosen_word:
    if world == guess:
        print("Right")
    else:
        print("wrong")