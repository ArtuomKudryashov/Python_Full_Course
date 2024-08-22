from datetime import *
my_date = date (2100, 4, 15)
print(my_date)

print(my_date.day)
print(my_date.year)
print(my_date.month)
print(my_date.isocalendar())
my_datetime = datetime(2222,6,10,14,55,59)
print(my_datetime)
print(my_datetime.microsecond)
print(my_datetime.isoformat())
print(my_datetime.now().microsecond)

print()
print("<<<<<<<<<<<Format Date>>>>>>>>>>>>>")
print(my_datetime.strftime('%d-%b-%Y'))
print(my_datetime.strftime('%d-%m-%Y'))
print(my_datetime.strftime('%d/%m/%Y'))
print(my_datetime.strftime('%d/%m/%Y %H:%M:%S'))

current_datetime = datetime.now()
print(current_datetime)
print(current_datetime.day)

date_str = '10/12/2222'
converted_date = datetime.strptime(date_str, '%d/%m/%Y')
print(converted_date)
