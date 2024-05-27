my_list =[1,2,3]

print(id(my_list))

other_list = [1,2,3]
print(id(other_list))

print(id([1,2,3]))

other_list.append(4)
print(my_list)
print(other_list)
