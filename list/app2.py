my_list = [True, "one" , 4 , bool, [3,False], 4.5]
print(my_list)

my_list.pop(3)
print(my_list)

print(len(my_list))
#1
print("#1")
print(my_list)
print(my_list[::-1])
print(my_list)
#2
print("#2")
print(my_list)
my_list.reverse()
new_my_list=my_list
print(new_my_list)
print(my_list)
#3
print("#3")
print(my_list)
new_list2 = list(reversed(my_list))
print(new_list2)
print(my_list)
#Create
print("Create")
my_laptops= ['hp_i5','hp_i7']
my_laptops2= ['Hp_Artuom','Hp_Veronika']
Full_list = my_list+my_laptops
print(my_list)
print(my_laptops)
print(Full_list)

my_list.extend(my_laptops2+my_laptops)

print(my_list)
