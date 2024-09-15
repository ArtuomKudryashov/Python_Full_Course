from functools import reduce


def subtract(a,b):
    print(a-b)


subtract(5,6)

subtract2 = lambda a,b: a-b

ls = list (range(0,101))
print(ls)

def get_sum_of_even(a):
    x=0
    for num in a:
        if num %2==0:

            x+=num
    return x

get_sum_of_even = reduce(lambda x,y: x+y,(num for num in ls if num %2==0))
get_sum_of_even2 = lambda x: sum(num for num in ls if num %2==0)



a="fsdfdijfijdsfjdsjfijidsfjsidjfidsjfids"
d = {
    k:a.count(k) for k in a

}
print (d)