def dict_to_list(dictionary):
    print(dictionary.items())
    for item in dictionary.items():
        print(item)
    items_list = []
    for key, value in dictionary.items():
        if isinstance(value, int):  # Проверяем, является ли значение целым числом
            value *= 2  # Умножаем целые числа на 2
        items_list.append((key, value))
    return items_list


# Пример использования:
my_dict = {
    'name': 'Alice',
    'age': 30,
    'is_student': False,
    'height': 5.5,
    'courses': ['Math', 'Science'],
    'address': {'city': 'New York', 'zip': '10001'},
    'graduation_year': None,
    1: 'one',
    (2, 3): [4, 5],
    True: 'yes',
    'empty_list': [],
    'nested_dict': {'key1': 'value1', 'key2': 'value2'},
    'tuple_key': ('a', 'b', 'c'),
    'float_number': 3.14,
    'set_key': {1, 2, 3}
}
my_list = dict_to_list(my_dict)
print(my_list)
