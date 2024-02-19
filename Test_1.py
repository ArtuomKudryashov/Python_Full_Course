# my_list = [1, 2,                  3]
# print(my_list)
#
# def remove_spaces(arr):
#     result = []
#     joined_string = ''  # Инициализируем пустую строку для объединения слов
#     for word in arr:
#         joined_string += word  # Добавляем каждое слово в строку без пробелов
#         result.append(joined_string)  # Добавляем текущее значение строки в результат
#     return result
#
# # Test the function
# input_array = ['i', 'have', 'no', 'space']
# arr = remove_spaces(input_array)
# print(arr)

def swap(st):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = ''
    for stri in st:
        if stri in vowels:
            result+=stri.upper()
        else:
            result += stri
    return result


input_str = "Hello World!"
output_str = swap(input_str)
print(output_str)  # Вывод: "HEllO WOrld!"


