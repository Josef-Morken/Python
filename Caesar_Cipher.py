alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text_input, shift_input):
  cipher_text = "" 
  for letter in text_input:
    position = alphabet.index(letter)
    new_position = position + shift_input
    if new_position > 25:
      new_position -= 26
    new_letter = alphabet[new_position]
    cipher_text += new_letter
  print(f"The encoded text is {cipher_text}")

def decrypt(text_input, shift_input):
  cipher_text = ""
  for letter in text_input:
    position = alphabet.index(letter)
    new_position = position - shift_input
    new_letter = alphabet[new_position]
    cipher_text += new_letter
  print(f"The decrypted text is {cipher_text}")

if direction == "encode":
  encrypt(text_input=text, shift_input=shift)

if direction == "decode":
  decrypt(text_input=text, shift_input=shift)