import re

test_password ='ASDrSfd!23t56'

def check_password(password):
    length_regexp = r"\S{8,}"
    length_pattern = re.compile(length_regexp)
    lowercase_pattern= re.compile(r"^.*[a-z]+.*$")
    uppercase_pattern= re.compile(r"^.*[A-Z]+.*$")
    number_pattern = re.compile(r"^.*[0-9]+.*$")
    special_symbol_pattern = re.compile("^.*[@#$%^&+=!]+.*$")
    no_whitespace_pattern = re.compile(r"^\S*$")

    if not re.fullmatch(no_whitespace_pattern,password):
        return (False, "No whitespaces allowed in the  password")

    if not re.fullmatch(length_pattern,password):
        return (False,"Password is too short. It must be at least 8 characters long.")

    if not re.fullmatch(lowercase_pattern,password):
        return (False,"Password must contain at least one lowercase letter.")

    if not re.fullmatch(uppercase_pattern,password):
        return (False,"Password must contain at least one uppercase letter.")
    if not re.fullmatch(number_pattern,password):
        return (False, "Password must contain at least one digit.")
    if not re.fullmatch(special_symbol_pattern,password):
        return (False, "Password must contain at least one special character(@, #, $, %, ^, &, +, =, !).")

    return (True, "Password is valid")

print("<<<<<<<<<<<<<<8>>>>>>>>>>>>>>")
print(check_password('asdfgdgffg   ASDF3242!&'))

# print(check_password(test_password))
print("<<<<<<<<<<<<<<1>>>>>>>>>>>>>>")
print(check_password('123'))
print("<<<<<<<<<<<<<<2>>>>>>>>>>>>>>")
print(check_password('12345678'))
print("<<<<<<<<<<<<<<3>>>>>>>>>>>>>>")
print(check_password('1234567a'))
print("<<<<<<<<<<<<<<4>>>>>>>>>>>>>>")
print(check_password('123456Ba'))
print("<<<<<<<<<<<<<<5>>>>>>>>>>>>>>")
print(check_password('asdbADGAG'))
print("<<<<<<<<<<<<<<6>>>>>>>>>>>>>>")
print(check_password('3234sfASDF'))
print("<<<<<<<<<<<<<<7>>>>>>>>>>>>>>")
print(check_password('asdf ASDF3242!&'))
print("<<<<<<<<<<<<<<8>>>>>>>>>>>>>>")
print(check_password('asdfgdgffg   ASDF3242!&'))

while True:
    password = input ("Please enter password: ")
    password_check_res = check_password(password)
    if password_check_res[0]:
        print(password_check_res[1])
        break
    print(password_check_res[1])
