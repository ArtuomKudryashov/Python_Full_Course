import re

test_password ='ASDrSfd!23t56'

def check_password(password):
    length_regexp = r"\S{8,}"
    length_pattern = re.compile(length_regexp)
    lowercase_pattern= re.compile(r"[a-z]+")
    uppercase_pattern= re.compile(r"[A-Z]+")
    number_pattern = re.compile(r"[0-9]+")
    special_symbol_pattern = re.compile("[@#$%^&+=!]+")

    if not re.search(length_pattern,password):
        return (False,"Password is too short. It must be at least 8 characters long.")

    if not re.search(lowercase_pattern,password):
        return (False,"Password must contain at least one lowercase letter.")

    if not re.search(uppercase_pattern,password):
        return (False,"Password must contain at least one uppercase letter.")
    if not re.search(number_pattern,password):
        return (False, "Password must contain at least one digit.")
    if not re.search(special_symbol_pattern,password):
        return (False, "Password must contain at least one special character(@, #, $, %, ^, &, +, =, !).")

    return (True, "Password is valid")

# print(check_password(test_password))
print(check_password('123'))
print(check_password('12345678'))
print(check_password('1234567a'))
print(check_password('123456Ba'))
print(check_password('asdbADGAG'))
print(check_password('3234sfASDF'))
print(check_password('asdfASDF3242!&'))
