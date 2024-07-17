import time
start_time = time.time()
my_range = range(1000000000)
print(my_range[1000])
end_time = time.time()
differenceR = end_time - start_time

print("Total; duration of the operation: ", differenceR)
start_timeL = time.time()
my_list = list(range(1000000000))
print(my_list[1000])
end_timeL = time.time()
differenceL= end_timeL-start_timeL
print("Total; duration of the operation: ", differenceL)
print()
print("The time difference between the executions of the operations is", differenceL-differenceR)