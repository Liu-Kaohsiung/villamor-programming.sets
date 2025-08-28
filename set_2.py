def shift_letter(letter, shift):
  if letter == " ":
    return " "
  alphabet_index = ord(letter) - ord('A')
  shifted_index = (alphabet_index + shift) % 26
  return chr(ord('A') + shifted_index)

def caesar_cipher(message, shift):
  result = ""
  for char in message:
    result += shift_letter(char, shift)
  return result

def shift_by_letter(letter, letter_shift):
  if letter == " ":
    return " "
  shift_amount = ord(letter_shift) - ord('A')
  alphabet_index = ord(letter) - ord('A')
  shifted_index = (alphabet_index + shift_amount) % 26
  return chr(ord('A') + shifted_index)

def vigenere_cipher(message, key):
    result = ""
    key_index = 0
    for char in message:
        if char == " ":
            result += " "
        else:
            shift_amount = ord(key[key_index % len(key)]) - ord('A')
            result += shift_letter(char, shift_amount)
            key_index += 1
    return result

def scytale_cipher(message, shift):
    # Pad message
    while len(message) % shift != 0:
        message += "_"
    n = len(message)
    result = ""
    for i in range(n):
        result += message[(i // shift) + (n // shift) * (i % shift)]
    return result

def scytale_decipher(message, shift):
    n = len(message)
    result = [""] * n
    for i in range(n):
        original_index = (i // (n // shift)) + (i % (n // shift)) * shift
        result[original_index] = message[i]
    return "".join(result)
