button_info ={
    'text': 'Buy',

}

button_style = {
    'color':'yellow',
    'width': 200,
    'height':300
}
button = {
    **button_info,
    **button_style
}

print(button)

button2 = button_info|button_style
print(button2)