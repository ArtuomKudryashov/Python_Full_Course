set1={13,17,18,28,46,4,444,4444,890,987}
print(type(set))
set2={13,17,118,2238,446,4445,44324,443344,890,987}
commons = set1.intersection(set2)
print(commons)
dif= set1.difference(set2)
print(dif)
dif2= set2.difference(set1)
print(dif2)
difsim = set1.symmetric_difference(set2)
print(difsim)

list_1= list(set1)
print(list_1)
list_2= list(set2)
print(list_2)