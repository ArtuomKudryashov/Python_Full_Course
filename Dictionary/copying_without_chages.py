from  copy import deepcopy

info = {
    'name':'Artuom',
    'is_instructor': True
}
info_copy = info.copy()
info_copy['review_qty'] = 5

print(info_copy)

print(info)

info = {
    'name': 'Artuom',
    'is_instructor':True,
    'reviews':[]

}
info_copy = info.copy()
info_copy['reviews'].append('Great course!')

print(info)
print(info_copy)
print( len(info))
print( len(info_copy))