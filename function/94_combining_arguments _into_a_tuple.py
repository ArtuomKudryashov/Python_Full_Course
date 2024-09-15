def create_tuple(*args):
    print(type(args))
    print(args)
    print(args[0])
    return sum(args)


result = create_tuple(1, 2, 3)
print(result)  # Output: (1, 2, 3)

