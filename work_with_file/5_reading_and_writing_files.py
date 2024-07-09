from pathlib import Path
import os
test_file3 = open('text.txt','w')
with open ('text.txt') as test_file:
    print(test_file.read())

# with open('test.txt') as test_file:
#     print(test_file.readlines())


print("<<<<<<<<<<<Writing  to file>>>>>>>>>>>>>")

with open('new.txt', 'w') as new_file:
    new_file.write("First line in the new file\n")

with open('new.txt') as new_file:
    print(new_file.read())


with open('new.txt', 'a') as new_file:
    new_file.write("Second line in the new file\n")

with open('new.txt') as new_file:
    print(new_file.read())


print("Delete File")
print(Path('new.txt').exists)

Path('new.txt').unlink()
print(Path('new.txt').exists())