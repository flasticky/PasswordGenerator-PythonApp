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
 
while True:   
    minLength = int(input("Enter the length (min. length 5, max. length 100): "))
    if minLength >= 5 and minLength <= 100:
        break
    else:
        print("Your password is too long or too short.")

if minLength < 10:
    print("WARNING - Your password is too short. Please consider a longer password for better security.\n")

while True:
    containsNumber = input("Do you want to include numbers (y/n)? ").lower()
    if containsNumber == "y" or containsNumber == "n":
        break
    else:
        print("Please enter 'y' for yes or 'n' for no.")

while True:
    containsSpecial = input("Do you want to include special characters (y/n)? ").lower()
    if containsSpecial == "y" or containsSpecial == "n":
        break
    else:
        print("Please enter 'y' for yes or 'n' for no.")

secret = generatePassword(minLength, containsNumber == "y", containsSpecial == "y")
print("The generated password is:", secret)
