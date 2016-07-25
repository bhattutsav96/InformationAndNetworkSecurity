# permutation keys
init_p = (2, 6, 3, 1, 4, 8, 5, 7)
init_p_inverse = (4, 1, 3, 5, 7, 2, 8, 6)
p10 = (3, 5, 2, 7, 4, 10, 1, 9, 8, 6)
p8 = (6, 3, 7, 4, 8, 5, 10, 9)
extraction_p = (4, 1, 2, 3, 2, 3, 4, 1)

# substitution boxes
S0 = [[1, 0, 3, 2],
      [3, 2, 1, 0],
      [0, 2, 1, 3],
      [3, 1, 3, 2]]
S1 = [[0, 1, 2, 3],
      [2, 0, 1, 3],
      [3, 0, 1, 0],
      [2, 1, 0, 3]]


# various functions which are self-explanatory
def permutate(original_input, fixed_key):
    return ''.join(original_input[i - 1] for i in fixed_key)


def get_L(bits):
    return bits[:int(len(bits) / 2)]


def get_R(bits):
    return bits[int(len(bits) / 2):]


def circular_left_shift(bits):
    return get_L(bits)[1:] + get_L(bits)[0] + get_R(bits)[1:] + get_R(bits)[0]


def find_key1(key):
    return ''.join(permutate(circular_left_shift(permutate(key, p10)), p8))


def find_key2(key):
    return ''.join(permutate(circular_left_shift(circular_left_shift(circular_left_shift(permutate(key, p10)))), p8))


def xor(arg1, arg2):
    return ''.join(str(((x + y) % 2)) for x, y in zip(map(int, arg1), map(int, arg2)))


def switch(bits):
    return get_R(bits) + get_L(bits)


def substitute_bits(four_bits, substitution_box):
    row = int(four_bits[0] + four_bits[3], 2)
    col = int(four_bits[1] + four_bits[2], 2)
    return '{0:02b}'.format(substitution_box[row][col])


def function_k(ip_bits, key):
    # functionk = (L xor F(R xor key),R)
    L = get_L(ip_bits)
    R = get_R(ip_bits)
    extracted_R = permutate(R, extraction_p)
    F = xor(extracted_R, key)
    substituted_bits = substitute_bits(get_L(F), S0) + substitute_bits(get_R(F), S1)
    return xor(L, substituted_bits) + R
    # return xor(get_L(ip_bits), substitute_bits(get_L(xor(permutate(get_R(ip_bits), extraction_p), key)), S0) + substitute_bits(get_R(xor(permutate(get_R(ip_bits), extraction_p), key)), S1)) + get_R(ip_bits)


def encrypt(plainText, key):
    ip = permutate(plainText, init_p)  # R1
    f1 = function_k(ip, find_key1(key))  # R2
    switched = switch(f1)  # R3
    f2 = function_k(switched, find_key2(key))  # R4
    ip_inverse = permutate(f2, init_p_inverse)  # R5
    return ip_inverse


def decrypt(cipherText, key):
    ip = permutate(cipherText, init_p)  # R1
    f2 = function_k(ip, find_key2(key))  # R2
    switched = switch(f2)  # R3
    f1 = function_k(switched, find_key1(key))  # R4
    ip_inverse = permutate(f1, init_p_inverse)  # R5
    return ip_inverse


plainText = '10100101'
key = '0010010111'
print("PlainText: " + plainText)
print("Key: " + key)
print("Key 1: " + find_key1(key))
print("Key 2: " + find_key2(key))
cipherText = encrypt(plainText, key)
print("Cipher text: " + cipherText)
print("Decrypted text: " + decrypt(cipherText, key))
