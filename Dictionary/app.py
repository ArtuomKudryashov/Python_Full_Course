my_motobike = {
    'brand':'Duccati',
    'price':25000,
    'engine_vol':1.2

}
my_motobike2 = {
    'brand':'Duccati',
    'price':25000,
    'engine_vol':1.2

}
if my_motobike and my_motobike2 and my_motobike == my_motobike2:
    print("Словари равны.")
else:
    print("Словари не равны.")
# print(my_motobike['brand'])
#
# my_motobike['price'] = 7000
# print(my_motobike)
#
# my_motobike['is_new'] = True
# print(my_motobike)
#
# del my_motobike ['engine_vol']
# print(my_motobike)
#
#
# key_name= 'brand'
# my_motobike[key_name]='BMW'
# print(my_motobike)

for item in my_motobike.items():
    key, value = item
    print(item)
    print(key)
    print(value)
    print(type(item))


my_motobike2 = {
    'brand':'BMW',
    'price_INFO':{'price':5000,
                  'is_available': True
                  },
    'engine_vol':1.2
}
print(my_motobike2['price_INFO']['is_available'])
print(my_motobike2['brand'])
print(my_motobike2.get('brand'))

