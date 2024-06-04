my_object = {
    'x': 10,
    'y': True
}
for item in my_object.items():
    key, value = item
    print(key, value)
print("<<<<<<<<<<2>>>>>>>>")
my_dict = {'id': 324, 'title': 'test'}

for item in my_dict.items():
    print(item)
print("<<<<<<<<<<3>>>>>>>>")
for key, value in my_dict.items():
    print(key, value)
