#Hangman Project

import random
word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

display = []

for _ in chosen_word:
    display += "_"
print(display)
guess = input("Guess your letter \n").lower()


for word in chosen_word:
    if word == guess:
        print("Right")
    else:
        print("wrong")