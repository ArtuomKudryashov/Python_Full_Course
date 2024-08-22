
my_dict = {}


for _ in range(3):
    key = input("Введите название ключа: ")
    value = input("Введите значение для ключа {}: ".format(key))
    my_dict[key] = value

print(my_dict)

for item in  my_dict.items():
    key,value = item
    print(item)
    print(key)


print(my_dict['price'])
print(my_dict.get('price'))

my_dict['is_new']=True

del  my_dict['a']

brand = 'b'
my_dict[brand] = "Trek Marlin "
print("Получившийся словарь:", my_dict)

