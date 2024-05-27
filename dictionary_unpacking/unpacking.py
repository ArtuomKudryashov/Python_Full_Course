button = {
    'width': 200,
    'text' : 'Buy',
    'color':'grey'
}

red_button ={
    **button,
    'color': 'red'
}

red_button2= {
    'color':"Green",
    **button


}
print(red_button)
print(red_button2)
print(button)

person = {
    'name':'John',
    'age':30,
    'city': "New - York"
}
for item in person.items():
    key,value = item
    print(item)
    print(key)
    print(value)