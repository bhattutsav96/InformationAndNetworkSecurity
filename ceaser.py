# user input
plainText = ''.join(input("Enter the plain text:").split()).lower()
key = int(input("Enter the key:"))

# encryption is done here
encryptedText = ''
for i in plainText: encryptedText += chr(((ord(i) - 97 + key) % 26) + 97)
print("Encrypted text: %s" % encryptedText)

# decryption is done here
decryptedText = ''
for i in encryptedText: decryptedText += chr(ord(i) - key) if ord(i) - key >= 97 else  chr(26 + ord(i) - key)
print("Decrypted text: %s" % decryptedText)
