alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text_input, shift_input, direction_input):
  cipher_text = ""
  if direction_input == "encode":
    for letter in text_input:
      position = alphabet.index(letter)
      new_position = position + shift_input
      if new_position > 25:
        new_position = new_position % 26 #handles shift amounts above the limit of the alphabet
      new_letter = alphabet[new_position]
      cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")
  elif direction_input == "decode":
    for letter in text_input:
      position = alphabet.index(letter)
      new_position = position - shift_input
      new_letter = alphabet[new_position]
      cipher_text += new_letter
    print(f"The decrypted text is {cipher_text}")
  
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text_input=text, shift_input=shift, direction_input=direction)

    restart = input("Type 'yes' if you wish to contine, or 'no' to quite the program.")
    if restart == "no":
        should_continue = False
        print("Goodbye")