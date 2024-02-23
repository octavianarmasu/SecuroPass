import getpass


def readPass():
    password = getpass.getpass("Enter your password: ")
    # secret password
    return password


def reenterPass():
    password = getpass.getpass("Re-enter your password: ")
    return password


def isDigit(letter):
    if letter >= '0' and letter <= '9':
        return True
    return False


def isSpecial(letter):
    if isDigit(letter) == False and not (letter.islower()) and not (letter.isupper()):
        return True
    return False


def passCheck(password):
    required = {'upper': False, 'lower': False,
                'digit': False, 'special': False, 'length': False}
    # checking how strong is the password
    if len(password) >= 8:
        required['length'] = True
    for letter in password:
        if letter.islower():
            required['lower'] = True
        if letter.isupper():
            required['upper'] = True
        if isDigit(letter):
            required['digit'] = True
        if isSpecial(letter):
            required['special'] = True
    return required


def passStrength(n):
    # printing the strength of the password
    if n == 1:
        print("Very weak password!")
    elif n == 2:
        print("Weak password!")
    elif n == 3:
        print("Decent password!")
    elif n == 4:
        print("Strong password!")
    elif n == 5:
        print("Very strong password!")


print("Your password should contain a lower case letter," +
      "an upper case letter, a digit, a special character.")
print("It should be at least 8 characters long.")
password = readPass()
password2 = reenterPass()
while password != password2:
    print("Passwords don't match. Please try again")
    password = readPass()
    password2 = reenterPass()
requirementsMet = sum(value for value in passCheck(password).values())
passStrength(requirementsMet)
# password will not be stored :)
password = ""
password2 = ""
