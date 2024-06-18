def filter_list(list_to_filter, value_type):
    def check_element_type(elem):
        return isinstance(elem, value_type)
    return list(filter(check_element_type,list_to_filter))


res= filter_list([1,10,"abc",5.5],int)

print(res)
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Вывод: [2, 4, 6]

def filter_list2(list_to_filter, value_type):
     return list(filter(lambda elem: type(elem)is value_type, list_to_filter))
