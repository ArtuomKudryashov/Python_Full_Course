import re
email_regexp = r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$"
email_check_pattern = re.compile(email_regexp)
print(email_check_pattern.fullmatch('academic198405@gmail.com'))
print(email_check_pattern.fullmatch('academic198405gmail.com'))
print(email_check_pattern.fullmatch('academic198405@gmailcom'))
print(email_check_pattern.fullmatch('@gmail.com'))
print(email_check_pattern.fullmatch('academic198405@'))
print(email_check_pattern.fullmatch('academi_c198405@gmail.com'))
print(email_check_pattern.fullmatch('academic.198405@gmail.com'))

print("<<<<<<<<<<<<<<<<<<<Function>>>>>>>>>>>>>>>>>>>>>>>")


def check_email(email):
    email_regexp1 = r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$"
    email_check_pattern1 = re.compile(email_regexp1)
    validation_result = "valid" if email_check_pattern1.fullmatch(email) else "not valid"
    return (email, validation_result)



print(check_email('academic198405@gmail.com'))
print(check_email('academic198405gmail.com'))
print(check_email('academic198405@gmailcom'))
print(check_email('@gmail.com'))
print(check_email('academic198405@'))
print(check_email('academi_c198405@gmail.com'))
print(check_email('academic.198405@gmail.com'))
