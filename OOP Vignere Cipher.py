# Vigenere Cipher_Marquez Francis Ivan B._BSCpE 1-5
# Vigenere Cipher by BasselTech https://www.youtube.com/watch?v=m04k32-QaAc
# Window tabs by Bro Code https://www.youtube.com/watch?v=4bMU1xAolSg

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
def _encrypt_decrypt_char(plaintext_char, key_char, mode='encrypt'):
    if plaintext_char.isalpha():
        first_alphabet_letter = 'a'
        if plaintext_char.isupper():
            first_alphabet_letter = 'A'

        old_char_position = ord(plaintext_char) - ord(first_alphabet_letter)
        key_char_position = ord(key_char.lower()) - ord('a')

        if mode == 'encrypt':
            new_char_position = (old_char_position + key_char_position) % 26
        else:
            new_char_position = (old_char_position - key_char_position + 26) % 26
        return chr(new_char_position + ord(first_alphabet_letter))
    return plaintext_char
# encrypt
def encrypt(plaintext, key):
    ciphertext = ''
    padded_key = _pad_key(plaintext, key)
    for plaintext_char, key_char in zip(plaintext, padded_key):
        ciphertext += _encrypt_decrypt_char(plaintext_char, key_char)
    return ciphertext
# decrypt
def decrypt(ciphertext, key):
    plaintext = ''
    padded_key = _pad_key(ciphertext, key)
    for ciphertext_char, key_char in zip(ciphertext, padded_key):
        plaintext += _encrypt_decrypt_char(ciphertext_char, key_char, mode='decrypt')
    return plaintext
# user input
plaintext = input('Enter a message: ')
key = input('Enter a key: ')
# output
ciphertext = encrypt(plaintext, key)
decrypted_plaintext = decrypt(ciphertext, key)

# additional
# window tabs

# import
from tkinter import *
from tkinter import ttk

window = Tk()
#tab manager
notebook = ttk.Notebook(window)
# add tabs
tab1 = Frame(notebook)
tab2 = Frame(notebook)
# add text to tabs
notebook.add(tab1,text="Vigenere Cipher")
notebook.add(tab2,text="Plaintext")
notebook.pack(expand=True,fill="both")
                                     
# output
Label(tab1,text=ciphertext,width=50,height=25).pack()
Label(tab2,text=decrypted_plaintext,width=50,height=25).pack()

window.mainloop()
