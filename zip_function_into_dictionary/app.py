fruits= ['apple','banana','lime','watermelon','grape']
quantities = [100,70,50,20,14]

availability = [True, False,False,True,False]

quantities_str=("12345")


fruit_qtys_zip = zip(fruits,quantities,availability,quantities_str)

print(fruit_qtys_zip)

fruit_qtys_list = list (fruit_qtys_zip)
print(fruit_qtys_list)