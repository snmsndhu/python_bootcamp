#Caesar Cipher Project
#In this project we are going to build a project that can encode and decode the message

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode to decrypt: \n")
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number: \n"))



def encrypt(plain_text, shift_amount):
  encrypted_message = ""
  for char in plain_text:
    position = letters.index(char)
    new_position = position + shift_amount
    new_letter = letters[new_position]
    encrypted_message += new_letter
  print(f"The encoded text is {encrypted_message}")
    

encrypt(text, shift)