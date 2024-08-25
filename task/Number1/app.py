name = input("Please, enter your name:  ")
lastname = input("Please, enter your lastname:  ")


name = name.lower()
print(f'My name is {name}')

lastname = lastname.lower()
print(f'My last name is {lastname}')

lastname = lastname.capitalize()
name = name.capitalize()
print(f'My last name is {lastname}')
print(f'My name is {name}')

lastname= lastname.upper()
name= name.upper()
print(f'My name is {name}')
print(f'My last name is {lastname}')

first_number = int(input("Please, enter firstNumber: "))
second_number = int(input("Please, enter secondNumber: "))
result = first_number+second_number

print(f'Summ {first_number} and {second_number} equals {result}')