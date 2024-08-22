list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print(combined_list)


my_list = [1, 2, 3]
another_list = [4, 5, 6]
my_list.extend(another_list)
print(my_list)

my_list2= [1,2,3,4,5,5,6,6,2,3,4,5]
print(my_list2.count(5))
print(my_list2.count(3))
print(my_list2.count(2))

first_two_my_list2 = my_list2[:2]
print(first_two_my_list2)

middle_ratings =my_list2[1:-1]
print(middle_ratings)

last_two_ratings = my_list2[-2:]
