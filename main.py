import random
import string

def generatePassword(minLength, numbers=True, specialCharacters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    
    print(letters, digits, special)
    
generatePassword(10)