import json

my_dict = {
    'name': 'John Doe',
    'age': 30,
    'is_student': False,
    'grades': [85, 90, 88],
    'address': {
        'street': '123 Main St',
        'city': 'Anytown',
        'zipcode': 12345
    },
    'contacts': {
        'email': 'john.doe@example.com',
        'phone': '+1234567890'
    }
}

json_str = json.dumps(my_dict, indent=1)
print(json_str)
print(type(json_str))

convert_to_dict= json.loads(json_str)
print(convert_to_dict)
print(type(convert_to_dict))
print(type(my_dict['address']['zipcode']))
