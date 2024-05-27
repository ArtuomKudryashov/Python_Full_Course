try:
    print(10/0)
except ZeroDivisionError as e:
    print(type(e))
    print(dir(e))
    print(e)
    print("<<<<<<<<<<>>>>>>>>>>>")
    print(e.__str__())

    print("Continue...")