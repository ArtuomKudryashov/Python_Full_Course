my_nums =(10,5,100,0,5,5,)

print(my_nums.count(5))
print(my_nums.index(5))


index_one = my_nums.index(5)
print(index_one)
index_two =my_nums.index(5,index_one+1)
print(index_two)
index_three = my_nums.index(5,index_two+1)
print(index_three)


my_list = list(my_nums)
my_list.append(7)
print(my_list)
print(my_nums)

my_nums=tuple(my_list)
print(my_nums)

my_touple = tuple('abcd')
print(my_touple)

my_touple2=tuple({


    "apple": "яблоко",
    "banana": "банан",
    "orange": "апельсин"
})
