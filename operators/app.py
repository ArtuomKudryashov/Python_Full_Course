set_one = {5,4.3, 2 , 6}
set_two = {5,4.3, 2,  6}

print(set_one == set_two)

print(set_one.__eq__(set_two))

print(set_one is set_two)
print(6 in  set_one)
print(6 in  set_two)
print(67 in  set_two)

print(not(6 in  set_two))
print(not (not(6 in  set_two)))
print(not(66 in  set_two))
print(not (not(66 in  set_two)))