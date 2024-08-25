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

my_touple2=tuple(({
    "apple": "яблоко",
    "banana": "банан",
    "orange": "апельсин"
    },
    {'Brand': 'Trek',
     'Model': 'Marlin 4',
     'Year': '2021'
     },
))
print(my_touple2[1]['Model'])

list_my_touple2 = list(my_touple2)
print(list_my_touple2)
print(list_my_touple2[0]['orange'])


my_fruit = 'Apple'
my_other_fruit = 'Orange'
my_next_one = 'Pineapple'

list = [my_fruit,my_other_fruit,my_next_one]
print(list)
my_other_fruit_tuple =(my_fruit,my_other_fruit,my_next_one)
print(my_other_fruit_tuple)

my_fruit_set= {
    my_fruit, my_other_fruit,my_next_one
}
print(my_fruit_set)
my_fruit_object = {
    'first_fruit': my_fruit,
    'second_fruit': my_other_fruit,
    'third_fruit': my_next_one
}

print(my_fruit_object)
my_fruit_object.items()
