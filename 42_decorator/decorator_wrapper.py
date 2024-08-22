def decorator_function(original_fn):
    def wrapper_function():
        #Some actions before execution of the original_fn
        print("Executed before function")

        result = original_fn()

        # Some actions after execution of the original_fn

        print("Executed after function")

        return  result

    return wrapper_function

@decorator_function
def my_function():
    print("This is my function!")




my_function()