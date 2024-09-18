import random
import time


# def sum_ignore_non_numbers(items: list) -> int:
    # filtered_items = []
    # for i in items:
    #     if isinstance(i, (int, float)):
    #         filtered_items.append(i)
    #
    # return sum(filtered_items)
    #
    # count = 0
    # for i in items:
    #     if isinstance(i, (int, float)):
    #         count += i
    # return count



    # return sum(i for i in items if isinstance(i, (int, float)))


    # return sum(i for i in items if type(i) in (int, float))
#
#
# print(sum_ignore_non_numbers([1, 2, 'Hey', None, 4.3, True]))
#
#
# def is_triangle(a, b, c):
#     return a + b > c and a + c > b and b + c > a
#
#
# print(is_triangle(2, 4, 9))
# print(is_triangle(3, 4, 5))
# #
#
# def average(*args):
#     if len(args) == 0:
#         return 0
#     return sum(args) / len(args)
#
#
# print(average())
#
#
# def common_strings(list1, list2, ignore_case=True):
#     lst = []
#     if ignore_case:
#         for i in list1:
#             for j in list2:
#                 if i.lower() == j.lower():
#                     lst.append(i.lower())
#     else:
#         for i in list1:
#             for j in list2:
#                 if i == j:
#                     lst.append(i)
#
#     return lst
#
#
# fruit_1 = ["banana", "APPLE", "watermelon", "cherry"]
# fruit_2 = ["Mango", "apple", "orange", "cherry"]
#
# print(common_strings(fruit_1, fruit_2))
# print(common_strings(fruit_1, fruit_2, ignore_case=False))
#
#
# def upper_lower(text):
#     lst = []
#     for i in range(len(text)):
#         if i % 2 == 0:
#             lst.append(text[i].upper())
#         else:
#             lst.append(text[i].lower())
#
#     return "".join(lst)
#
#
# text = input()
# print(upper_lower(text))
#
#
# def upper_lower2(text):
#     str = ""
#     for i in range(len(text)):
#         if i % 2 == 0:
#             str = str + text[i].upper()
#         else:
#             str = str + text[i].lower()
#
#     return str
#
#
# text = input()
# print(upper_lower2(text))
#
# sum_square = lambda x, y: x ** 2 + y ** 2
# print(sum_square(3, 4))
#
#
# def sum_square2(x, y):
#     return x ** 2 + y ** 2
#
#
# print(sum_square2(3, 4))
#
#
# def rec(s):
#     print(s)
#     s += 1
#     if s == 10:
#         return None
#
#     return rec(s)
#
#
# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     a, b = 0, 1
#     for i in range(2, n + 1):
#         a, b = b, a + b
#     return b
#
#
# print(fib(10))
#
#
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1 or n == 2:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# print(fibonacci(10))
#
#
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)
#
#
# print(factorial(5))

# print("<<<<<<<<<<<<Decorator>>>>>>>>>>>>")
#
# def timing_decorator(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func (*args,**kwargs)
#         end_time = time.time()
#         result_time = end_time - start_time
#         func_name= func.__name__
#         print((f"Function {func_name} took {result_time:.6f}"))
#
#         return result
#     return wrapper
# @timing_decorator
# def buble_sort(array):
#     n =len(array)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if array[j]> array[j+1]:
#                 array[j], array[j+1] = array[j+1], array[j]
#
#     return array
#
# def quick_sort_helper(array):
#     if len(array)<=1:
#         return array
#     a = array[len(array)//2]
#     left=[i for i in array if i< a]
#     middle = [i for i in  array if i ==a]
#     right = [i for i in  array if i >a]
#     return  quick_sort_helper(left) + middle + quick_sort_helper(right)
#
# @timing_decorator
# def quick_sort(array):
#     return  quick_sort_helper(array)
# def generate_random_list(n):
#     return [random.randint(1, n) for _ in range(n)]
#
#
# lst = generate_random_list(100000)
# # print(lst)
# #
# # buble_sort(lst)
# # print(quick_sort_helper(lst))
# quick_sort(lst)