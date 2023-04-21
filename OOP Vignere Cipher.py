# Vigenere Cipher_Marquez Francis Ivan B._BSCpE 1-5
# Vigenere Cipher by BasselTech https://www.youtube.com/watch?v=m04k32-QaAc

# adding characters
def _pad_key(plaintext, key):
    padded_key = ''
    i = 0
    for char in plaintext:
        if char.isalpha():
            padded_key += key[i % len(key)]
            i += 1
        else:
            padded_key += ' '
    return padded_key
# getting positions
# encrypt
# decrypt
# user input
plaintext = gkhkjh4560
print(padded_key)
# output
# additional