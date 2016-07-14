# importing shuffle from random to shuffle the key list
from random import shuffle

# user input
plainText = ''.join(input("Enter the plain text:").split()).lower()

# key generation and shuffling
key = [chr(i) for i in range(97, 123)]
shuffle(key)
print("Key : %s  " % key)

# encryption is done here
encryptedText = ''
for i in plainText: encryptedText += key[ord(i) - 97]
print("Encrypted text: %s" % encryptedText)

# decryption is done here
decryptedText = ''
for i in encryptedText: decryptedText += chr(key.index(i) + 97)
print("Decrypted text: %s" % decryptedText)
