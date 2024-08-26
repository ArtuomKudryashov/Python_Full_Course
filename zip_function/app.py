fruits= ['apple','banana','lime','watermelon']
quantities = [100,70,50,20]

availability = [True, False,False,True]

quantities_str=("1234")


fruit_qtys_zip = zip(fruits,quantities,quantities_str)

print(fruit_qtys_zip)

fruit_qtys_zip = list(fruit_qtys_zip)
print(fruit_qtys_zip)
car = {
    "brand": "Toyota",
    "model": "Camry",
    "year": 2020,
    "color": "blue",
    "engine": "V6"
}
print(list(car))
print(tuple(car))
print(set(car))
