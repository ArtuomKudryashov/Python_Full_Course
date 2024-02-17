def greeting(greet):
    return lambda name: f"{greet}, {name}!"


morning_greeting = greeting("Good Morning")

print(morning_greeting('Artuom'))


evening_greeting = greeting("Good Evening")
print(evening_greeting('Artuom'))


def add(x):
    return lambda y: x + y

add_five = add(5)
print(add_five(3))  # Выведет: 8

add_ten = add(10)
print(add_ten(3))   # Выведет: 13
