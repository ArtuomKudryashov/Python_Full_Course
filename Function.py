def my_fn(a,b):
    c = a + b
    return "Сумма а и b = " + str (c)

print(my_fn(5,6))

def my_fn2(a,b):
    c = a + b
    return f"Сумма a и b = {c}"

print(my_fn2(5,6))

name = "Artuom"
print (dir(name))

#input
name= input("Enter your name: ")
print(name)

print(name.capitalize())

print(name)
print(name.upper())
print(dir(__builtins__))
