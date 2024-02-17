list_int = [1,3,5,7,9,11,11,23,23,45,6,-5]
print(list_int[::-1])

el= list_int[3]
print(el)

list_int[3]=152
print(list_int)

my_tuple = tuple(list_int)
print(my_tuple)

print(my_tuple[3])


my_set= set(my_tuple)
my_set.add(2305)
print(my_set)
list_str = 'Artuom'
my_list = list(list_str)
print(my_list)
#for

greeting = "Hello Artuom!"
count_0 = 0
for char in  greeting:
    if char == 'l':
        count_0=count_0+1

print(count_0)

def format_date(*,day:int, month:str)->str:
    return  f'The date : {day} of {month}'

print(format_date(day=17, month= "February"))


def customer_greeting(*, name:str, greeting:str)->str:
    return  f"{greeting},{name}"


print(customer_greeting(name="Artuom", greeting="Hi"))
