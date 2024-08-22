import time
print(time)
print(time.time())
start_time= time.time()
print(time.ctime(2345234523))

time.sleep(2)
end_time = time.time()
print(end_time-start_time)