my_dict={
    "a":15,
    "b":17,
    "c":20,
    "d":"Artuom",
    "e":100,
    "f":114
}
print("<<<<<<<<<<<<<<<<<<<<<<<<<<LIST>>>>>>>>>>>>>>>>>>>>>>>>")
print("if  v % 2==0 and all value ")
even_num=[(v *10 if isinstance(v,int)and  v %2 ==0 else v) for  k,v in  my_dict.items()]
print(even_num)
print(type(even_num))

print("Only digital")
even_num2 = [(v * 10 if v % 2 == 0 else v) for v in my_dict.values() if isinstance(v, int)]
print(even_num2)
print(type(even_num2))

print("<<<<<<<<<<<<<<<<<<<<<<<<<<TUPLE>>>>>>>>>>>>>>>>>>>>>>>>")
print("if  v % 2==0 and all value ")
even_num3 = ((v * 10 if isinstance(v, int) and v % 2 == 0 else v) for k, v in my_dict.items())
even_num3_tuple = tuple(even_num3)
print(even_num3_tuple)
print(type(even_num3_tuple))

print("Only digital")
even_num4 = ((v * 10 if v % 2 == 0 else v) for v in my_dict.values() if isinstance(v, int))
even_num4_tuple = tuple(even_num4)
print(even_num4_tuple)
print(type(even_num4_tuple))


print("<<<<<<<<<<<<<<<<<<<<<<<<<<SET>>>>>>>>>>>>>>>>>>>>>>>>")
print("if  v % 2==0 and all value ")
even_num5 = {(v * 10 if isinstance(v, int) and v % 2 == 0 else v) for k, v in my_dict.items()}

print(even_num5)
print(type(even_num5))

print("Only digital")
even_num6 = {(v * 10 if v % 2 == 0 else v) for v in my_dict.values() if isinstance(v, int)}
print(even_num6)
print(print(type(even_num6)))

print("<<<<<<<<<<<<<<<<<<<<<<<<<<DICTIONARY>>>>>>>>>>>>>>>>>>>>>>>>")
even_num7 ={k:v for k,v in my_dict.items()}
print(even_num7)
even_num8 = {k:(v*10 if isinstance(v, int) and v % 2 == 0 else v) for k, v in my_dict.items()}
print(even_num8)
print(type(even_num8))


even_num9 = {k:(v*10 if v % 2 == 0 else v) for k, v in my_dict.items() if isinstance(v, int)}
print(even_num9)
print(type(even_num9))

even_num10 = {k:(v*10 ) for k, v in my_dict.items() if isinstance(v, int)and v % 2 == 0}
print(even_num10)
print(type(even_num10))


print("<<<<<<<<<<<<<<<<<UPPER>>>>>>>>>>>>>>>>>")
even_num11 = {
    k: (v * 10 if isinstance(v, int) and v % 2 == 0 else v.upper() if isinstance(v, str) else v)
    for k, v in my_dict.items()
}
print(even_num11)
print(type(even_num11))


my_list = ["Artuom", "MARLIN","TREK","33","345"]

my_list2= [elem for elem  in my_list if len(elem)>=3]
print(my_list2)

my_list3 = ["Artuom", "MARLIN","TREK","33","345"]

my_list4= [elem for elem  in my_list if len(elem)>=3 and 'R' in elem]
print(my_list4)

