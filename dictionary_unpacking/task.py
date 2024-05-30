family = {
    'name': 'Artuom',
    'name1': 'Veranika'
}

artuom = {
    'vecivleA':'bike',
    'brandA' : 'Marlin 4'
}

veranika = {
    'vecivleV': 'bike',
    'brandV': 'Schwinn 29'
}

list_of_dict1 = [family, artuom, veranika]

family_dict, artuom_dict, veranika_dict = list_of_dict1
print("<<<<<<1>>>>>>")
print(family_dict)
print(artuom_dict)
print(veranika_dict)
print()
print("<<<<<<<<<2>>>>>>>>")
def unpack_dictionary(person_dict, vehicle_dict):
    for key, value in person_dict.items():
        print(f"Name: {value}")

    for key, value in vehicle_dict.items():
        print(f"Vehicle: {value}")


unpack_dictionary(family, artuom)
unpack_dictionary(family, veranika)

print("<<<<<<<<<3>>>>>>>>")
def unpack_dictionary1(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

unpack_dictionary1(**family)
unpack_dictionary1(**artuom)
unpack_dictionary1(**veranika)

print("<<<<<<<<<4>>>>>>>>")
def unpack_dict(arg1, arg2):
    return f"Этот Bike {arg1} бренда {arg2}"


print(unpack_dict(veranika['vecivleV'], veranika['brandV']))
