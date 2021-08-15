import re
from encrypter import *
from decrypter import *

def encrypt(string):
    #Split the user text
    splitted = list(string)
    #Replace the letters
    encrypted = to_encrypt(splitted)
    #Join the list elements to get a encrypted string
    foruser = ''.join(encrypted)
    return foruser

def decrypt(string):
    #Split the letter in nth spaces. Here n is 2
    splitted = re.findall('..?',string)
    #Take the two letters and find the approriate letter and replace it
    decrypted = to_decrypt(splitted)
    #Join the elements and return a decrypted string
    foruser = ''.join(decrypted)
    return foruser

## Asking User for the text and the operation they want to perform
while True:
    print("Select operation you want to perform?")
    print("1. Encryption \n2. Decryption \nEnter '1' or '2' \n3. Exit")
    option = int(input("> "))
    if option == 1:
        text = str(input("Enter the text you want to encrypt: \n"))
        print("Your encrypted text is: \n",encrypt(text))
    elif option ==2:
        text = str(input("Enter text you want to decrypt: \n"))
        print("Your decrypted text is: \n",decrypt(text))
    elif option == 3:
        break
    else:
        print("Enter either '1' or '2'")
