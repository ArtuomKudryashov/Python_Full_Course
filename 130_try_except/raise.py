def divide_nums(a , b):
    if b == 0:
        raise TypeError("Second argument can't be 0")
    return a/b


try:
    divide_nums(10,0)
# except ZeroDivisionError as e:
#     print(e)
except TypeError as e:
    print(e)

print('Continue')
    