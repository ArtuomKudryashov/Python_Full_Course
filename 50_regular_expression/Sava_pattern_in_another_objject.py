import re
my_string = "My name is Artuom."
other_string = "My name is Artuom!"


# my_pattern = re.compile(r"A....m\.$")
my_pattern = re.compile(r"^My.*\.$")
print(my_pattern)
print(my_pattern.search(my_string))
print(my_pattern.match(my_string))
print(my_pattern.match(other_string))
print("<<<<<<<<<<<Case2>>>>>>>>>>>")
my_string = "My name is Artuom. Artuom is instructor"
my_pattern = re.compile(r"A....m")
print(my_pattern)
print(my_pattern.findall(my_string))


