# function that will return row and column no of the given char from the matrix
def get_pair(char):
    for x, y in enumerate(matrix):
        if char in y:
            return x, y.index(char)


# function that returns encryption of given two chars
def encrypt(char1, char2):
    row1, col1 = get_pair(char1)
    row2, col2 = get_pair(char2)
    for i in range(0, len(preProcessedText), 2):
        if row1 == row2:
            encrypted_chars = matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            encrypted_chars = matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            encrypted_chars = matrix[row1][col2] + matrix[row2][col1]
    return encrypted_chars


# function that returns decryption of given two chars
def decrypt(char1, char2):
    row1, col1 = get_pair(char1)
    row2, col2 = get_pair(char2)
    for i in range(0, len(encryptedText), 2):
        if row1 == row2:
            decrypted_chars = matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            decrypted_chars = matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:
            decrypted_chars = matrix[row1][col2] + matrix[row2][col1]
    return decrypted_chars


# user input
plainText = list(''.join(input("Enter the plain text:").split()).lower())
key = list(''.join(input("Enter the key:").lower().split()))
key.extend(chr(i) for i in range(97, 123))
seen = set()
key = [k for k in key if not (k in seen or seen.add(k))]
key.remove('j')

# matrix generation
matrix = []
for i in range(0, len(key), 5): matrix.append(key[i:i + 5])
for i in matrix: print(i)

# preprocessing of the plain text
preProcessedText = [w.replace('j', 'i') for w in plainText]
running = True
count = 0
while running:
    if (count + 1 < len(preProcessedText) and preProcessedText[count] == preProcessedText[
            count + 1]): preProcessedText.insert(count + 1, 'z')
    count += 2
    if count >= len(preProcessedText): running = False
if len(preProcessedText) % 2 == 1: preProcessedText.append('z')

# encryption is done here
encryptedText = ''
for i in range(0, len(preProcessedText), 2): encryptedText += encrypt(preProcessedText[i], preProcessedText[i + 1])
print("Encrypted text: %s" % encryptedText)

# decryption is done here
decryptedText = ''
for i in range(0, len(encryptedText), 2): decryptedText += decrypt(encryptedText[i], encryptedText[i + 1])
print("Decrypted text: %s" % decryptedText)
