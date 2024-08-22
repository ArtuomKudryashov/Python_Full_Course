def decorator_function(original_fn):
    def wrapper_function():
        result = original_fn()
        return result
    return wrapper_function


@decorator_function
def my_function():
    print("This is my function!")


my_function()
