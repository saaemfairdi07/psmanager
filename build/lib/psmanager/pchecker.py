def checkSpecialCharacters(password):
    specialCharacter = ["~","`","!","@","#","$","%","^","&","*","_"]
    for symbol in specialCharacter:
        if symbol in str(password):
            return True

strength = {
    "strength": str()
}
def checkPasswordLength(password):
    length = len(password)
    if (length >= 6 and length <= 16):
        if length <= 8:
            strength["strength"] = "Weak"
        elif length <= 12:
            strength["strength"] = "Moderate"
        elif length <= 16:
            strength["strength"] = "Strong"
        return True
    print("This password is too long to remember...")

def checkNums(password):
    numberList = ["1","2","3","4","5","6","7","8","9","0"]
    for number in numberList:
        if number in str(password):
            return True

def checkPasswordStrength(password):
    if (checkSpecialCharacters(password) and checkPasswordLength(password) and checkNums(password)):
        return True,f'{strength["strength"]}'
    else:
        return False,"Password must be 6 or more characters long, and must contain special symbols and numbers..."