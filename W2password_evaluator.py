#Password Checker
#Create a program which evaluates a password based on a set of rules and gives users feedback about
#their password in order to improve it.
#Password Strength Criteria:
#Weak:
#- The password is less than 8 characters long.
#- The password only contains lowercase or uppercase letters (not both).
#Moderate:
#- The password is at least 8 characters long.
#- The password contains both uppercase and lowercase letters.
#- The password contains at least one numeric digit.
#Strong:
#- The password is at least 12 characters long.
#- The password contains both uppercase and lowercase letters.
#- The password contains at least one numeric digit.
#- The password contains at least one special character (e.g., !, @, #, etc.)


password = input("Please enter a password: ")

lowercase = any(char.islower() for char in password)
uppercase = any(char.isupper() for char in password)
numeric = any(char.isdigit() for char in password)
special = any(not char.isalnum() for char in password)

match password:
    case n if len(password) >= 12 and lowercase and uppercase and numeric and special:
        print("strong password")

    case n if len(password) >= 8 and lowercase and uppercase and numeric:
        print("moderate password")

    case n if len(password) < 8 or not (lowercase and uppercase):
        print("weak password")

    case _:
        print("Password doesn't meet any specific category, please do not use space.")
