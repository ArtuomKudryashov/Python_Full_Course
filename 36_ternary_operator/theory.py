my_number =21

print("is int") if  type(my_number) is int else print ("is not int")

if type(my_number)is  int:
    print("is int")
else:
    print("is not int")

"""ex2.

send_img(img)  if img.get['is_processed']  else process_and_sernd_img(img)
"""

#Ex3

product_qty=10

print ("in stock" if product_qty>0 else"out of stock")

#Ex4

temp = +24
weather = "hot" if temp>18 else "cold"
print(weather)