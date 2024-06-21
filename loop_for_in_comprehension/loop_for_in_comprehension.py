all_nums = [-3,1,0,10,-20,5]

absolute_nums = []

for num in all_nums:
    absolute_nums.append((abs(num)))

print(absolute_nums)
print(all_nums)


absolute_nums2 = [abs(num) for num in all_nums]

print(absolute_nums2)

print("<<<<<<<<<<<<<<<<<<<<<<<<2>>>>>>>>>>>>>>>>>>>>>>>")

positive_nums = []

for num in all_nums:
    if num >0:
        positive_nums.append(num)

print((positive_nums))


positive_nums2 = [num for num in all_nums if num >0]

print( positive_nums2)

print("<<<<<<<<<<<<<<<<<<<<<<<<Set>>>>>>>>>>>>>>>>>>>>>>>")
my_set = {1,10,15}
new_set = set()

for val in my_set:
    new_set.add(val*val)
print(my_set)
print(new_set)

new_set2={el*el for el in my_set}
print(new_set2)

new_set3=[el*el for el in my_set if el%3==0]
print(new_set3)

print("<<<<<<<<<<<<<<<<<<<<<<<<Dictionary>>>>>>>>>>>>>>>>>>>>>>>")

my_scores = {
    'a':10,
    'b':7,
    'm':14
}
# for keys in my_scores.keys():
#     print(keys)
#
# for value in  my_scores.values():
#     print(value)

# for key, value in my_scores.items():
#     print(key)
#     print(value)
print("<<<<<<<<<<<<<<<1>>>>>>>>>>>>>>>")
for rek in my_scores.items():
    key, value = rek
    print(rek)
    # print(f"Key: {key}, Value: {value}")

print("<<<<<<<<<<<<<<<1.2>>>>>>>>>>>>>>>")

scores = {}

for key ,value in my_scores.items():
    scores[key] = value*10

print(scores)
print(my_scores)

print("<<<<<<<<<<<<<<<2>>>>>>>>>>>>>>>")


scores2 = {k:v *10 for k,v in my_scores.items()}
print(scores2)

print("<<<<<<<<<<<<<<<3>>>>>>>>>>>>>>>")

scores3 = {k:v *10 for k,v in my_scores.items()if v%7==0}
print(scores3)

print("<<<<<<<<<<<<<<<41>>>>>>>>>>>>>>>")


scores4 = {k: (v * 10 if v % 7 == 0 else v) for k, v in my_scores.items()}
print(scores4)

print("<<<<<<<<<<<<<<<5>>>>>>>>>>>>>>>")
scores5 = { (v * 10 if v % 7 == 0 else v) for k, v in my_scores.items()}
print(scores5)

print("<<<<<<<<<<<<<<<7>>>>>>>>>>>>>>>")

my_scores7 = [10,7,14]

scores8 = {index:elem *2 for  index, elem in enumerate (my_scores7)}
print(scores8)

