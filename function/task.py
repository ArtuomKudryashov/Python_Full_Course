def merge_list_to_dict(list_one, list_two):
    ziped_seq = zip(list_one,list_two)
    return  dict(ziped_seq)



res_one= merge_list_to_dict(['a','b','c'],[10,True, []])
print(res_one)


res_two = merge_list_to_dict(['abc'],[{},True,100])
print(res_two)

res_three= merge_list_to_dict([10,True,100], ['abc'])
print(res_three)


def sun_nums(*args):
    print(args)
    print(type(args))
    # print(args[0])
    return sum(args)

print(sun_nums())