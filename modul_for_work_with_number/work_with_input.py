import random

count = 0
n = int(input("Enter the number of iterations:: "))


for _ in range(n):
    print(random.randint(1, 10))

count = 0


while count < n:
    print(random.randint(1, 10))
    count += 1