#List
my_list = [True, 10, 'abc',{}]

for elem in my_list:
    print(elem)

#Tuple
video_info = ('1920x1080', True, 27)

for elem in video_info:
    print(elem)

#Dictionary

my_object = {
    'x':10,
    'y':True,
    'z':'abc'

}
for key in my_object:
    print(key, my_object[key])



my_object = {
    'x': 10,
    'y': True,
    'z': 'abc'
}

for key in my_object.keys():
    print(key)

my_object = {
    'x': 10,
    'y': True,
    'z': 'abc'
}

for value in my_object.values():
    print(value)


for el in [1,'abc',True]:
    print(type(el))
    print(el)


print(el)