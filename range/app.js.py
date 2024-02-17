my_range = range(5)
print(my_range)
print(type(my_range))
print(my_range[2])

print(my_range.start)
print(my_range.step)
print(my_range.stop)


for n in my_range:
    print(n)


for r in range(7):
    print(r)


for nRange in range (12,25,5):
    print(nRange)


print(list(range (12,25,5)))
print(tuple(range (12,25,5)))
print(set(range (12,25,5)))

my_range2 =  range(12,25,5)

print(my_range2.start)
print(my_range2.step)
print(my_range2.stop)

print(my_range2.index(22))
# print(my_range2.index(19))

print(my_range2.count(12))

print(my_range2.count(120))

my_range3 = range (2,50,3)

my_list = []
for el in my_range3:
    print(el)
    my_list.append(el)



print(my_list)
print(tuple(my_list))
print(set(my_list))



