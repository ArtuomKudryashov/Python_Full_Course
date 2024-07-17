import random
print(random.random())
print(random.randint(1,10))
print(random.choice('abcd'))
print(random.choice([1,10,4]))
print(random.choices([1,10,4,4,56,8,9],k=2))
print("<<<<<<<Shuffle>>>>>>>")
my_list = [1,10,4,4,56,8,9]

random.shuffle(my_list)
print(my_list)
random.shuffle(my_list)
print(my_list)





for _ in range(2):
    print(random.randint(1, 10))

n = 2
count = 0


while count < n:
    print(random.randint(1, 10))
    count += 1

n