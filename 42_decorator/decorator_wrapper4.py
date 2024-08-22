def decorator_function(original_fn):
    def wrapper_function(*args, **kwargs):
        print("Arguments passed to wrapper_function:")
        print("Positional arguments (args):", args)
        print("Keyword arguments (kwargs):", kwargs)
        print("Executed before function")

        result = original_fn(*args, **kwargs)

        print("Executed after function")
        return result

    return wrapper_function

@decorator_function
def my_function(a, b, c=None):
    print("Inside my_function")
    print(f"a = {a}, b = {b}, c = {c}")
    return (a, b, c)

# Вызываем декорированную функцию
result14 = my_function(100, 50, c="Hello")
print("Result14 returned by my_function:", result14)
