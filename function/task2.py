def merge_list_to_dict(list_one, list_two):
    ziped_seq = zip(list_one,list_two)
    return  dict(ziped_seq)



res_one= merge_list_to_dict(list_one=['a','b','c'], list_two=[10,True, []])
print(res_one)


res_two = merge_list_to_dict( list_two=[{},True,100],list_one=['abc'])
print(res_two)

res_three= merge_list_to_dict([10,True,100], list_two= ['abc'])
print(res_three)


def  update_car_info (**car):
    car['is_available'] =  True
    return car


res= update_car_info(brand = "BMW" , price= 100000)
print(res)
print(update_car_info(brand ="Audi", price = 10000))
print(update_car_info(brand ="Audi", price = 10000))


