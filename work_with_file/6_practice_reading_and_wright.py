test_file = open('test.txt','w')
print(test_file)
print(type(test_file))
test_file2=open(r'D:\Python\Python-Bogdan\work_with_file\test2.txt','w')
print(test_file2)
print(type(test_file2))


print("<<<<<<<<<<<<<<<<<<first way>>>>>>>>>>>>>>>>>>")
test_file = open ('test.txt', 'w')
test_file.write("First string\n")
test_file.write("Monkey Business\n")

test_file = open ('test.txt', 'w')
test_file.write('Rewrite\n')
test_file.close()

test_file=open('test.txt')
print(test_file.read())

test_file.close()

print("<<<<<<<<<<<<<<<<<<second  way>>>>>>>>>>>>>>>>>>")
with open('test2.txt','w') as test_file2:
    test_file2.write("First string\n")
    test_file2.write("Monkey Business\n")
    test_file2.write("Chiki\n")

test_file2= open('test2.txt')
print(test_file2.read())
test_file2.close()

print("<<<<<<<<<<Third way>>>>>>>>>>>>>")
# test_file3 = open('test3.txt','w')



with open('test3.txt', 'w') as test_file3:
    test_file3.write("First string\n")
    test_file3.write("Monkey Business\n")
    test_file3.write("Chiki\n")
    test_file3.write("\n")

    test_file3.write("for cripe's sake; shizit!\n")


with open('test3.txt') as test_file3:
    print(test_file3.read())

with open('test3.txt', 'a') as test_file3:
    test_file3.write("Second line in the new file\n")


with open('test3.txt') as test_file3:
    print(test_file3.read())


print("<<<<<<<<<<Read all lines>>>>>>>>>>>>>")
with open('test3.txt') as test_file3:

    lines = test_file3.readlines()

for line in lines:
    print(line)

print("<<<<<<<<<<Read all lines-2>>>>>>>>>>>>>")
with open('test3.txt') as test_file3:
    print(test_file3.readlines())



print("<<<<<<<<<<Read all lines REFACTOR>>>>>>>>>>>>>")
with open('test3.txt') as test_file3:
    for line in test_file3:
        print(line)

print("<<<<<<<<<<Read line>>>>>>>>>>>>>")
with open('test3.txt') as test_file3:
    print(test_file3.readline())
    print(test_file3.readline())
    print(test_file3.readline())
    print(test_file3.readline())
    print(test_file3.readline())
    print(test_file3.readline())
    res = (test_file3.readline())
    print(res)
    print(type(res))
    print(res=='')



print("<<<<<<<<<<Read line in WHILE>>>>>>>>>>>>>")
with open('test3.txt') as test_file3:
    while True:
        line=test_file3.readline()
        print(line)
        if not line:
            break





with open('text3.py', 'w') as test_file4:
    test_file4.write("#Hello\n")
    test_file4.write("f='Hello'\n")
    test_file4.write("a = 5\n")
    test_file4.write("b = 5\n")
    test_file4.write("c = a + b\n")
    test_file4.write("print(f)\n")
    test_file4.write("print('Sum a and b equal:', c)\n")
    test_file4.write("print(b)")


with open('text3.py', 'r') as test_file4:
    code = test_file4.read()


exec(code)

