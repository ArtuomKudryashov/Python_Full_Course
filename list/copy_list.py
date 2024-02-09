my_cars = ['BMW', 'Mersedes']
copied_cars = my_cars
copied_cars.append('Audi')

print(my_cars)
print(copied_cars)
print(copied_cars == my_cars)
#slice
my_cars2 = ['BMW', 'Mersedes']
copied_cars2 = my_cars2[:]
copied_cars2.append('Audi')

print(my_cars2)
print(copied_cars2)
print(copied_cars2 == my_cars2)

#Copy
my_cars3 = ['BMW', 'Mersedes']
copied_cars3 = my_cars3.copy()
copied_cars3.append('Audi')

print(my_cars3)
print(copied_cars3)
print(copied_cars3 == my_cars3)

#list
my_cars4 = ['BMW', 'Mersedes']
copied_cars4 = list(my_cars4)
copied_cars4.append('Audi')

print(my_cars4)
print(copied_cars4)
print(copied_cars4 == my_cars4)


