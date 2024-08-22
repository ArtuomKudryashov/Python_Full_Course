import json

json_str = '{"id":235, "brand":"Nike", "qty":84,"status":{"isForSale":true}}'

sneakers = json.loads(json_str)

print(type(sneakers))
print(sneakers['brand'])
print(sneakers['qty'])
print(sneakers['status']['isForSale'])

print(sneakers)

json_array='[1,2,3]'

my_list = json.loads(json_array)
print(my_list)


json_array2='[{"a":1},{"b":2},{"c":3}]'

my_list2 = json.loads(json_array2)
print(my_list2)