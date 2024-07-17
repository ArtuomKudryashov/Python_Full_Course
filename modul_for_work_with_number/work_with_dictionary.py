import random

print("<<<<<<<<<Selecting random keys from the dictionary:>>>>>>>>>>>>")


my_dict = {'a': 1, 'b': 10, 'c': 4, 'd': 4, 'e': 56, 'f': 8, 'g': 9}


# Extracting keys
keys = list(my_dict.keys())


# Select 2 random keys
random_keys = random.choices(keys, k=2)
print(random_keys)

print("<<<<<<<<<Selecting random values from the dictionary:>>>>>>>>>>>>")

my_dict = {'a': 1, 'b': 10, 'c': 4, 'd': 4, 'e': 56, 'f': 8, 'g': 9}


values = list(my_dict.values())


random_values = random.choices(values, k=2)
print(random_values)


print("<<<<<<<<<<Selecting random pairs (key, value) from the dictionary>>>>>>>>>>>")
my_dict = {'a': 1, 'b': 10, 'c': 4, 'd': 4, 'e': 56, 'f': 8, 'g': 9}


items = list(my_dict.items())

random_items = random.choices(items, k=2)
print(random_items)