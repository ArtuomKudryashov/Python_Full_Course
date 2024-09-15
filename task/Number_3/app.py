from task.helper import *

# task(1)
# list_number_divisible_by_two_numbers(2, 3, 101)
#
# list_number_divisible_by_two_numbers_for(2, 3, 101)
#
# task(2)
# items = [1.2, 3, None, 100, {'info': 'bla-bla'}, 44, 'Hi!', 99, 44.32, None]
# new_list = [x for x in items if isinstance (x,(int,float))]
#
# print(new_list)
# print(sum(new_list))
#
#
# list_2 = []
# summ = 0
# for x in items:
#     if isinstance(x, (int, float)):
#         list_2.append(x)
#         summ = summ+ x;
# print(list_2)
# print(summ)
#
# print ("<<<<<<<<<<<<<<<<<<Method-2>>>>>>>>>>>>>>>>")
# filter_number_divided_two_three(items)
# task(3)
# #
# # list_message=[]
# # while True:
# #     message = input("Please, Speak to me: ")
# #     list_message.append(message)
# #     if len(list_message)>5:
# #         del (list_message[0])
# #     if message == "Пока!":
# #         print("Ну ладно пока!")
# #
# #         break
# #     print(list_message)
#
#
# get_five_message()
#
# task(4)
# numbers = [15, 3, 8, 42, 3, 23, 8, 7, 42, 1, 9, 23, 15, 5, 9, 4, 6, 1]
# result = set(numbers)
# print(type(result))
# result_list = list(result)
# print(type(result_list))
# (result_list.sort())
# print(result_list)
#
# print("<<<<<<<<<<<<<<<<<<<<<<<<<<<2>>>>>>>>>>>>>>>>>>>>>>>>>")
#
# numbers = [15, 3, 8, 42, 3, 23, 8, 7, 42, 1, 9, 23, 15, 5, 9, 4, 6, 1]
# result = set(numbers)
# print(type(result))
# result_list = list(result)
# print(result_list)
# print(type(result_list))
#
#
# sort_list = sorted(result_list)
# print(sort_list)
#
# print(result_list)
#
# print("<<<<<<<<<<<<<<<<<<<<<<<<<<<3_For>>>>>>>>>>>>>>>>>>>>>>>>>")
# numbers = [15, 3, 8, 42, 3, 23, 8, 7, 42, 1, 9, 23, 15, 5, 9, 4, 6, 1]
# result = set(numbers)
# print(type(result))
# result_list = list(result)
# for i  in range(len(result_list)):
#     for j in  range (len(result_list)-1):
#         if(result_list[j]>result_list[j+1]):
#             result_list[j],result_list[j+1]=result_list[j+1],result_list[j]
#
# print(result_list)
#
#
# print("<<<<<<<<<<<<<<<<<<<<<<<<<<<4_For_Temp>>>>>>>>>>>>>>>>>>>>>>>>>")
# numbers = [15, 3, 8, 42, 3, 23, 8, 7, 42, 1, 9, 23, 15, 5, 9, 4, 6, 1]
# result = set(numbers)
# print(type(result))
# result_list = list(result)
# print(result_list)
# for i  in range(len(result_list)):
#     for j in  range (len(result_list)-1):
#         if (result_list[j] > result_list[j + 1]):
#             temp =result_list[j]
#             result_list[j]= result_list[j+1]
#             result_list[j+1]=temp
#
# print(result_list)
#
#
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<5_Sort_withoutSet_For_Temp>>>>>>>>>>>>>>>>>>>>>>>>>")
#
numbers = [15, 3, 8, 42, 3, 23, 8, 7, 42, 1, 9, 23, 15, 5, 9, 4, 6, 1]
# new_list_number=[]
# for i  in range(len(numbers)):
#     for j in  range (len(numbers)-1):
#         if (numbers[j] > numbers[j + 1]):
#             temp = numbers[j]
#             numbers[j]= numbers[j+1]
#             numbers[j+1]=temp
#
#
# for i in range(len(numbers)):
#     if i == len(numbers) - 1 or numbers[i] != numbers[i + 1]:
#         new_list_number.append(numbers[i])
#
# print("Отсортированный список:", numbers)
# print("Уникальные элементы:", new_list_number)

sorted(numbers)

print("<<<<<<<<<<<<<<<<<<<<<<<<<<<6_Sort_withoutSet_For_Temp>>>>>>>>>>>>>>>>>>>>>>>>>")

numbers = [15, 3, 8, 42, 3, 23, 8, 7, 42, 1, 9, 23, 15, 5, 9, 4, 6, 1]
new_list_number=[]
for i  in range(len(numbers)):
    for j in  range (len(numbers)-1):
        if (numbers[j] > numbers[j + 1]):
            temp = numbers[j]
            numbers[j]= numbers[j+1]
            numbers[j+1]=temp


for num in numbers:
    if num not in new_list_number:
        new_list_number.append(num)

print("Отсортированный список:", numbers)
print("Уникальные элементы:", new_list_number)