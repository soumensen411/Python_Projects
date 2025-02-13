import random 
import string

chars =' ' + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)
# print(f'Chars : {chars}')
# print(f'key:{key}')

#ENCRYPT
plain_text = input('Enter a message to encrypt: ')
cipher_text = ""
for latter in plain_text:
    index = chars.index(latter)
    cipher_text+=key[index]

print(f'Orginal massage: {plain_text}')
print(f'Encrypted massage: {cipher_text}')

# Decrypt
cipher_text = input('Enter a message to encrypt: ')
plain_text = ""
for latter in cipher_text:
    index = key.index(latter)
    plain_text+=chars[index]

print(f'Encrypted massage: {cipher_text}')
print(f'Orginal massage: {plain_text}')