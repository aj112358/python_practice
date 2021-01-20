# Exercise 73: Caesar Cipher

LOWER = [chr(i) for i in range(ord('a'), ord('z')+1)]
UPPER = [chr(i) for i in range(ord('A'), ord('Z')+1)]

shift = int(input("What shift (between -25 and +25): "))
plaintext = input("What's the message: ")
ciphertext = ""

for letter in plaintext:
    if letter.islower():
        ciphertext += LOWER[(LOWER.index(letter) + shift) % 26]
        # ciphertext += chr((ord(letter) + shift) % 65)
    elif letter.isupper():
        ciphertext += UPPER[(UPPER.index(letter) + shift) % 26]
    else:
        ciphertext += letter

print(ciphertext)
