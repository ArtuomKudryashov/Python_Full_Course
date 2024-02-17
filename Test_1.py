my_list = [1, 2,                  3]
print(my_list)

def remove_spaces(arr):
    result = []
    space_count = 0
    for word in arr:
        word_without_spaces = ''.join(arr)
        result1 = result.append(word_without_spaces)
    return result

# Test the function
input_array = ['i', 'have', 'no', 'space']

arr= remove_spaces(input_array)
print(arr)
