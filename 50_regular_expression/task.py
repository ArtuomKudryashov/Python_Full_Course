import re

def check_password(password):
    if len(password) < 8:
        return "Password is too short. It must be at least 8 characters long."

    if not re.search("[a-z]", password):
        return "Password must contain at least one lowercase letter."

    if not re.search("[A-Z]", password):
        return "Password must contain at least one uppercase letter."

    if not re.search("[0-9]", password):
        return "Password must contain at least one digit."

    if not re.search("[@#$%^&+=!]", password):
        return "Password must contain at least one special character (@, #, $, %, ^, &, +, =, !)."

    return "Password successfully accepted!"

user_password = input("Enter your password: ")
result = check_password(user_password)
print(result)
