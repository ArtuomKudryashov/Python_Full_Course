import random
import secrets
import string

print(random.choices('0123456789',k=8))
print(''.join(random.choices('ABCDF0123456789', k=8)))
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.punctuation)

print(string.ascii_letters+string.digits+string.punctuation)

all_chars =string.ascii_letters+string.digits+string.punctuation
my_password=secrets.choice(all_chars)
print(my_password)
print(secrets.choice(all_chars)for i in range(8))
my_password2 = ''.join(secrets.choice(all_chars) for i in range(20))
print(my_password2)

