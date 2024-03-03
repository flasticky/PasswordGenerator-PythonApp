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
    
    while len(secret) < minLength or not meetsCriteria:
        secret = ""
        containsNumber = False
        containsSpecial = False
        
        for _ in range(minLength):
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
    while True:   
        minLength = int(input("Enter the length (min. length 5, max. length 100): "))
        if minLength >= 5 and minLength <= 100:
            break
        else:
            if minLength < 5:
                print("Your password is too short.")
            else:
                print("Your password is too long.")

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
            
    while True:
        try:
            numberOfPasswords = int(input("How many passwords do you want to generate (min. 1, max. 100)? "))
            if numberOfPasswords >= 1 and numberOfPasswords <= 100:
                break
            else:
                print("Please enter a valid number (min. 0, max. 100)")
        except ValueError:
            print("Please enter a valid number (min. 0, max. 100)")

    if numberOfPasswords == 1:
        print("\nGenerated password:")
    else:
        print("\nGenerated passwords:")
    for _ in range(numberOfPasswords):
        secret = generatePassword(minLength, containsNumber == "y", containsSpecial == "y")
        print(secret)
    print()
