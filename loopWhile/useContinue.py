import random

random_num = random.randint(1,3)
while True:
    num = int(input("Guess the number from 1 to 3"))
    if num != random_num:
        print("try again...")
        continue

    print("Congratulations!", random_num)
    break