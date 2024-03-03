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
        if specialCharacters:
            meetsCriteria = meetsCriteria and containsSpecial
    
    return secret
    
minLength = int(input("Enter the length: "))
if minLength < 10:
    print("WARNING - Your password is too short. Please choose a longer password for better security.")
containsNumber = input("Do you want to include numbers (y/n)? ").lower() == "y"
containsSpecial = input("Do you want to include special characters (y/n)? ").lower() == "y"
secret = generatePassword(minLength, containsNumber, containsSpecial)
print("The generated password is:", secret)
