import math
def calc_factorial(num):
    if type(num) is not int:
        raise TypeError ("Number must be integer")
    if num <= 0:
        raise ValueError("Number must be positive")
    if num ==1 or num==0:
        return 1
    return calc_factorial(num-1)*num


print(calc_factorial(10))
print(math.factorial(10))

def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_seq = fibonacci_recursive(n - 1)
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq

# Пример использования:
result = fibonacci_recursive(8)
print("Последовательность Фибоначчи до 8 элемента:", result)