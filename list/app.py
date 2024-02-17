my_nums = [10, 50, 0, 5,5, 100]
print(dir(my_nums))

res = my_nums.count(5)
print(res)

my_nums.append(25)
print(my_nums)

my_nums.insert(2,154)
print(my_nums)

my_nums.clear()
print(my_nums)

print("Delete")
my_list = [1, 2, 3, 6]
my_list[3:5] = [1500, 2500,3500,4500,5500,6500]
print(my_list)

my_list.remove(2)
print(my_list)


#del
del my_list[2]
print(my_list)

#pop()
my_list.pop(2)
print(my_list)
el=my_list.pop(3)
print(el)
print(my_list)

