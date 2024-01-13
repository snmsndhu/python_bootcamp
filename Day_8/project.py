#Caesar Cipher Project
#In this project we are going to build a project 
#that can encode and decode the message

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input("Type 'encode' to encrypt, type 'decode to decrypt: \n")
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number: \n"))

shift = shift % 26

def caesar(plain_text, shift_amount, direction_selection):
  end_message = ""
  if direction_selection == "decode":
      shift_amount *= -1
  for char in plain_text:
    if char in letters:
        letter_position = letters.index(char)
        new_position = letter_position + shift_amount
        end_message += letters[new_position]
    else:
       end_message += char
  print(f"The {direction_selection}d text is {end_message}")

  
  
caesar(text, shift, direction)
     