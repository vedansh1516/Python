def ceaser_encrypt(text,value):
 
  cipher = ''
  for char in text: 
    if char == ' ':
      cipher += char
    elif  char.isupper():
      cipher += chr((ord(char) + value - 65) % 26 + 65)
    else:
      cipher += chr((ord(char) + value - 97) % 26 + 97)

  return cipher
 
text = input("Enter string: ")
cipher = int(input("Enter shift cipher: "))
print("Encrypted output: ", ceaser_encrypt(text, cipher))