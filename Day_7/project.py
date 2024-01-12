#Hangman Project

import random
word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

display = []

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

    if "_" not in display:
      end_game = True
      print("you win")
   