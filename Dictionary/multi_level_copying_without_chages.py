from copy import  deepcopy
info = {
    'name':'Artuom',
    'is_instructor': True
}
info_copy = info.copy()
info_copy['review_qty'] = 5

print(info_copy)

print(info)
print("<<<<<<<<<<<<one-level>>>>>>>>>>>>")

info = {
    'name': 'Artuom',
    'is_instructor':True,
    'reviews':[]

}
info_copy = info.copy()
info_copy['reviews'].append('Great course!')

print(info)
print(info_copy)
print("<<<<<<<<<<<<multi-level>>>>>>>>>>>>")

info = {
    'name': 'Artuom',
    'is_instructor':True,
    'reviews':[]
}
info_deepcopy=deepcopy(info)
info_deepcopy['reviews'].append('Great course!')
info_deepcopy['reviews'].append('Great course!')
info['reviews'].append('Super!')
info['new_key']=10

print(info)
print(info_deepcopy)
