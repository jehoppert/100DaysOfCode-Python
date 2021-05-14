#Caesar Cipher
import caesar_cipher_art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
  out_text = ""
  shift = shift % len(alphabet) #size to alphabet list
  for letter in text:
    if letter not in alphabet:
      out_text += letter
    elif direction == "encode":
      new_pos = alphabet.index(letter) + shift
      if new_pos >= len(alphabet):
        new_pos = new_pos - len(alphabet)
      out_text += alphabet[new_pos]
    elif direction == "decode":
      new_pos = alphabet.index(letter) - shift
      if new_pos < 0:
        new_pos = new_pos + len(alphabet)
      out_text += alphabet[new_pos]
  print(f"Text is {out_text}")

print(caesar_cipher_art.logo)
run = True
while run:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(text, shift, direction)
  cont = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")
  if cont != "yes":
    run = False
    print("Goodbye")
