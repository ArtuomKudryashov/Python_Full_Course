mixed_set = {2, 'hello', 3.14, True}
print(mixed_set)
mixed_set.add(6)
print(mixed_set)

mixed_set2= {2, 'hello', 3.14, 14, "False", False, bool,100}

common_set= mixed_set&mixed_set2
print(common_set)

list_set= list(common_set)
print(list_set)
print(tuple(common_set))