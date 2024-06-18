def filter_list(list_to_filter, value_type):
    filtered_list = []
    for element in list_to_filter:
        # if isinstance(element,value_type):
        if type(element) == value_type:
            filtered_list.append(element)

    return filtered_list

print(filter_list([35, True, 'abc', 10], int))
print(filter_list([35, True, 'abc', 10], str))
print(filter_list([35, True, 'abc', 10], bool))