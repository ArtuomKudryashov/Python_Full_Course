try:
    print(10 / 0)
except ZeroDivisionError as e:
    print(isinstance(e, Exception))
    print(e)
except TypeError as e:
    print(e)

print('Continue...')

try:
    print("10"/0)
except Exception as e:
    print(e)
    print("Continue")