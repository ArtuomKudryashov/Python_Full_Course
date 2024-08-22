import re
my_string = "My name is Artuom."
res = re.search("Artuom", my_string)
res2 = re.search("A....m", my_string)
res3 = re.search("^M.*A....m", my_string)
res4 = re.search("A....m.$", my_string)
res5 = re.search("A....m\\.$", my_string)
res5a = re.search(r"A....m\.$", my_string)

print(res)
print(res2)
print(res3)
print(res4)
print(res5)
print(res5a)
print(type(res))
print('A....m\n.$')
print(r'A....m\n.$')
print(res.span())
print(res4.span())
print(res5a.span())
print(res.start())
print(res.end())

