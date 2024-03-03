import random
import string

def generatePassword(minLength, numbers=True, specialCharacters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    
    characters = letters
    if numbers:
        characters += digits
    if specialCharacters:
        characters += special
        
    secret = ""
    meetsCriteria = False
    containsNumber = False
    containsSpecial = False
    
    while not meetsCriteria or len(secret) < minLength:
        newChar = random.choice(characters)
        secret += newChar
        
        if newChar in digits:
            containsNumber = True
        elif newChar in special:
            containsSpecial = True
            
        meetsCriteria = True
        if numbers:
            meetsCriteria = containsNumber
        if special:
            meetsCriteria = meetsCriteria and containsSpecial
    
    return secret
    
secret = generatePassword(10)
print(secret)