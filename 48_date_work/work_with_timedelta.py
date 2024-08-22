from datetime import datetime, timedelta

my_datetime = datetime(2222,12,10,18,10,45)
print(timedelta)
print(my_datetime)
print(my_datetime+timedelta(days=100))
print(my_datetime+timedelta(days=100,minutes=120))
print(my_datetime+timedelta(days=100,hours=3))
print(my_datetime-timedelta(days=100,hours=3))
