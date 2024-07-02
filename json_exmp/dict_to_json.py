import json

dict_data={
    'id': 235,
    'brand': 'Nike',
    'qty':84,
    'status':{ 'isForSale':True}
}

sneak_json = json.dumps(dict_data)
print(sneak_json)
print(type(sneak_json))

print("<<<<<<<<<<<<<<<<<2>>>>>>>>>>>>>>>>>>")

sneak_json2 = json.dumps(dict_data,indent=1)
print(sneak_json2)
print(type(sneak_json2))
print("<<<<<<<<<<<<<<<<<3>>>>>>>>>>>>>>>>>>")

sneak_str = json.loads(sneak_json)
print(sneak_str)
print(type(sneak_str))
print("<<<<<<<<<<<<<<<<<4>>>>>>>>>>>>>>>>>>")

json_from_dict=json.dumps(dict_data)
print(json_from_dict)
print(type(json_from_dict))
