
my_dict = {}


for _ in range(3):
    key = input("Введите название ключа: ")
    value = input("Введите значение для ключа {}: ".format(key))
    my_dict[key] = value


print("Получившийся словарь:", my_dict)

